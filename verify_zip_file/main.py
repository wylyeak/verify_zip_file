# coding=UTF-8
import sys
from threading import Thread

from PyQt4 import QtGui, QtCore

from mainwindow import Ui_main_window
from extractutil import IExtractShow
from verifyfile import VerifyFile, IVerifyFileShow
from util import *


class GUIVerifyFileShow(QtCore.QObject, IVerifyFileShow):
    show_info_signal = QtCore.pyqtSignal(dict)
    finish_verify_signal = QtCore.pyqtSignal(dict)

    def __init__(self):
        QtCore.QObject.__init__(self)

    def show_info(self, **kv_args):
        self.show_info_signal.emit(kv_args)

    def finish_verify(self, **kv_args):
        self.finish_verify_signal.emit(kv_args)


class GUIExtractFileShow(QtCore.QObject, IExtractShow):
    start_extract_signal = QtCore.pyqtSignal(dict)
    update_extract_signal = QtCore.pyqtSignal(dict)
    finish_extract_signal = QtCore.pyqtSignal(dict)

    def __init__(self):
        QtCore.QObject.__init__(self)

    def start_extract(self, **kv_args):
        self.start_extract_signal.emit(kv_args)

    def finish_extract(self, **kv_args):
        self.finish_extract_signal.emit(kv_args)

    def update_extract(self, **kv_args):
        self.update_extract_signal.emit(kv_args)


class MyItem(QtGui.QTreeWidgetItem):
    def __init__(self, kv_args=None, key=None, parent=None):
        super(MyItem, self).__init__(parent)
        if kv_args:
            self.kv_args = kv_args
            self.file_path = kv_args["file_path"]
            self.line_num = kv_args["line_num"]
            self.line = kv_args["line"]
            self.relative_file_path = kv_args["relative_file_path"]
            self.matcher = kv_args["matcher"]
        if key:
            self.key = key
        self.child_mapper = dict()
        self.leaf = False

    def add_child(self, q_tree_widget_item):
        self.child_mapper[q_tree_widget_item.key] = q_tree_widget_item
        QtGui.QTreeWidgetItem.addChild(self, q_tree_widget_item)

    def get_child(self, key):
        return self.child_mapper.get(key)


class MainWindow(QtGui.QMainWindow, IExtractShow, IVerifyFileShow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.start_button.clicked.connect(self.__start_verify)
        self.flag = False
        self.analyze_info = GUIVerifyFileShow()
        self.analyze_info.show_info_signal.connect(self.show_info)
        self.analyze_info.finish_verify_signal.connect(self.finish_verify)
        self.extract_progress = GUIExtractFileShow()
        self.extract_progress.start_extract_signal.connect(self.start_extract)
        self.extract_progress.finish_extract_signal.connect(self.finish_extract)
        self.extract_progress.update_extract_signal.connect(self.update_extract)
        self.model = MyItem()
        self.ui.tree_view.setColumnCount(2)
        self.ui.tree_view.setHeaderLabels([u"文件", u"行号"])
        self.ui.tree_view.clicked.connect(self.item_clicked)

    def __show_status_msg(self, msg):
        self.ui.status_bar.showMessage(unicode(msg))

    def finish_walk(self):
        self.flag = False
        self.__show_status_msg(u"分析完成")

    def show_info(self, kv_args):
        file_path = kv_args["file_path"]
        line_num = kv_args["line_num"]
        line = kv_args["line"]
        relative_file_path = kv_args["relative_file_path"]
        matcher = kv_args["matcher"]
        dir_nodes = list(relative_file_path.split(os.sep))
        dir_nodes.append(str(line_num))
        parent = self.model
        index = 0
        total = len(dir_nodes)
        for dir_node in dir_nodes:
            tmp = parent.get_child(dir_node)
            if tmp:
                pass
            else:
                if self.model == parent:
                    tmp = MyItem(kv_args, dir_node, self.ui.tree_view)
                    tmp.setText(0, unicode(dir_node))
                else:
                    tmp = MyItem(kv_args, dir_node, parent)
                    if index + 1 == total:
                        tmp.setText(0, parent.key)
                        tmp.setText(1, unicode(dir_node))
                        tmp.leaf = True
                    else:
                        tmp.setText(0, unicode(dir_node))
                parent.add_child(tmp)
            parent = tmp
            index += 1
        print "show_info", file_path, line_num, line, matcher, relative_file_path

    def start_extract(self, kv_args):
        self.ui.progress_bar.setMinimum(0)
        self.ui.progress_bar.setMaximum(kv_args["uncompress_size"])
        self.ui.progress_bar.setValue(0)
        self.__show_status_msg(u"正在解压 " + spit_filename(kv_args["fp"], True))

    def finish_extract(self, kv_args):
        self.ui.progress_bar.setValue(self.ui.progress_bar.maximum())
        self.__show_status_msg(u"完成解压 " + spit_filename(kv_args["fp"], True))

    def update_extract(self, kv_args):
        self.ui.progress_bar.setValue(kv_args["extract_size"])

    def finish_verify(self, kv_args):
        self.flag = False
        self.model = MyItem()

    def item_clicked(self, model_index):
        print model_index.model()

    def __start_verify(self):
        if not self.flag:
            if os.path.isfile(str(self.ui.zip_path.text())):
                self.flag = True
                vf = VerifyFile(str(self.ui.zip_path.text()), str(self.ui.work_path.text()), "config.ini", True,
                                self.analyze_info, self.extract_progress)
                thread = Thread(target=vf.walk)
                thread.setDaemon(True)
                thread.start()
            else:
                print "path is"
                # self.flag = False
        else:
            self.__show_status_msg(u"正在工作中， 请稍后")
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())