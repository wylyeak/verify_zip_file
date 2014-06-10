# coding=UTF-8
import sys
from threading import Thread

from PyQt4 import QtGui, QtCore

from mainwindow import Ui_main_window
from core.extractutil import IExtractShow
from core.verifyfile import VerifyFile, IVerifyFileShow
from core.util import *
from core.setting import *


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

    def get_children(self):
        return list(self.child_mapper.values())

    def clear(self):
        self.child_mapper = dict()

    def add_child(self, q_tree_widget_item):
        self.child_mapper[q_tree_widget_item.key] = q_tree_widget_item

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
        self.vf = None
        self.ui.config_path.clicked.connect(self.change_config)
        self.analyze_info = GUIVerifyFileShow()
        self.analyze_info.show_info_signal.connect(self.show_info)
        self.analyze_info.finish_verify_signal.connect(self.finish_verify)
        self.extract_progress = GUIExtractFileShow()
        self.extract_progress.start_extract_signal.connect(self.start_extract)
        self.extract_progress.finish_extract_signal.connect(self.finish_extract)
        self.extract_progress.update_extract_signal.connect(self.update_extract)
        self.ui.zip_path.textChanged.connect(self.text_changed)
        self.model = MyItem()
        self.ui.tree_view.itemSelectionChanged.connect(self.item_selected)
        exclude_file_action = QtGui.QAction(u"排除文件", self.ui.tree_view)
        exclude_file_action.triggered.connect(self.exclude_file)
        self.ui.tree_view.addAction(exclude_file_action)
        exclude_txt_action = QtGui.QAction(u"排除字符", self.ui.tree_view)
        exclude_txt_action.triggered.connect(self.exclude_txt)
        self.ui.tree_view.addAction(exclude_txt_action)
        self.ui.tree_view.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.ui.tree_view.header().setStretchLastSection(True)
        self.setting = None
        self.config_path = None
        self.__init_settings()

    def change_config(self):
        f_name = QtGui.QFileDialog.getOpenFileNameAndFilter(self.ui.central_widget, u"选择一个文件", os.path.curdir,
                                                            "*.ini")
        if f_name[0]:
            self.__set_config_path(unicode(f_name[0]))

    def text_changed(self, text):
        if self.ui.work_path.text() == text:
            pass
        else:
            if os.path.isfile(text):
                self.__set_config_path(self.setting.get_file_config_path(spit_filename(text, True)))
            else:
                self.__show_status_msg(u"ZIP文件路径错误")

    def __set_config_path(self, config_path, show=True):
        if config_path and not os.path.isabs(config_path):
            config_path = os.path.join("..", "config", config_path)
        if config_path and os.path.isfile(config_path):
            self.ui.config_path.setText(spit_filename(config_path, True))
            self.config_path = config_path
            if show:
                self.__show_status_msg(u"配置文件已自动加载为：" + spit_filename(config_path, True))
        else:
            if config_path:
                self.__show_status_msg(config_path + u"不存在")
            self.__set_config_path(self.setting.get_default_config(), False)
            self.__show_status_msg(u"未配置专属配置文件，加载默认配置文件config.ini")

    def __init_settings(self):
        setting_path = ".." + os.sep + "config" + os.sep + "setting.ini"
        if os.path.isfile(setting_path):
            self.setting = Setting(setting_path)
            self.ui.work_path.setText(unicode(self.setting.get_work_path()))
            self.__set_config_path(self.setting.get_default_config())
        else:
            self.__show_status_msg("未找到setting.ini文件")

    def __show_status_msg(self, msg):
        self.ui.status_bar.showMessage(unicode(msg))

    def show_info(self, kv_args):
        line_num = kv_args["line_num"]
        relative_file_path = kv_args["relative_file_path"]
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
                    tmp_parent = self.ui.tree_view
                else:
                    tmp_parent = parent
                tmp = MyItem(kv_args, dir_node, tmp_parent)
                if index + 1 == total:
                    tmp.setText(0, parent.key)
                    tmp.setText(1, dir_node)
                else:
                    tmp.setText(0, dir_node)
                if index + 2 >= total:
                    tmp.leaf = True
                parent.add_child(tmp)
            parent = tmp
            index += 1

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
        self.__show_status_msg(u"文件分析完成")

    def exclude_file(self):
        item = self.ui.tree_view.currentItem()
        text = ""
        if item and item.leaf:
            text = spit_filename(item.file_path, True)
        text, ok = self.__make_input_dialog(u"排除文件", u"正则表达式写法", text)
        text = str(text).strip()
        if ok and self.vf and text != "":
            self.vf.eu_file.add_regex(text)
            self.__show_status_msg(u"添加排除文件成功")
        else:
            self.__show_status_msg(u"添加排除文件失败")

    def exclude_txt(self):
        item = self.ui.tree_view.currentItem()
        text = ""
        if item and item.leaf:
            text = item.matcher
        text, ok = self.__make_input_dialog(u"排除字符", u"正则表达式写法", text)
        if ok and self.vf and text != "":
            self.vf.eu_text.add_regex(text)
            self.__show_status_msg(u"添加排除文本成功")
        else:
            self.__show_status_msg(u"添加排除文本失败")

    def __make_input_dialog(self, title, tip, default):
        dialog = QtGui.QInputDialog(self.ui.central_widget)
        dialog.setInputMode(QtGui.QInputDialog.TextInput)
        dialog.setLabelText(tip)
        dialog.resize(350, 127)
        dialog.setWindowTitle(title)
        dialog.setTextValue(default)
        ok = dialog.exec_()
        text = dialog.textValue()
        return tuple([text, ok])

    def item_selected(self):
        item = self.ui.tree_view.currentItem()
        if item and item.leaf:
            self.ui.text_view.select_anchor(item)
            if item.childCount() == 0:
                self.__show_status_msg(unicode(item.matcher))

    def __validate(self):
        zip_path = unicode(self.ui.zip_path.text())
        if not os.path.isfile(zip_path):
            self.__show_status_msg(u"ZIP文件不对")
            return False
        work_path = unicode(self.ui.work_path.text())
        if not os.path.isdir(work_path):
            self.__show_status_msg(u"解压路径不对")
            return False
        config_path = unicode(self.config_path)
        if not os.path.isfile(config_path):
            self.__show_status_msg(u"配置文件不对")
            return False
        return True

    def __start_verify(self):
        if not self.flag:
            if self.__validate():
                self.flag = True
                self.ui.tree_view.clear()
                self.vf = VerifyFile(unicode(self.ui.zip_path.text()), unicode(self.ui.work_path.text()),
                                     unicode(self.config_path),
                                     True,
                                     self.analyze_info, self.extract_progress)
                thread = Thread(target=self.vf.walk)
                thread.setDaemon(True)
                thread.start()
        else:
            self.__show_status_msg(u"正在工作中， 请稍后")
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())