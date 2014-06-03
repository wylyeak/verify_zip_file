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


class MainWindow(QtGui.QMainWindow, IExtractShow, IVerifyFileShow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.zip_path.setText(u"D:/work/pop-T-order.shop.jd.com-bjshijianwei-Zheng"
                                 u"Chang-test-r3012_2014-05-27_16.57.37.zip")
        self.ui.work_path.setText(unicode("D:\\work"))
        self.ui.start_button.clicked.connect(self.__start_verify)
        self.flag = False
        self.analyze_info = GUIVerifyFileShow()
        self.analyze_info.show_info_signal.connect(self.show_info)
        self.analyze_info.finish_verify_signal.connect(self.finish_verify)
        self.extract_progress = GUIExtractFileShow()
        self.extract_progress.start_extract_signal.connect(self.start_extract)
        self.extract_progress.finish_extract_signal.connect(self.finish_extract)
        self.extract_progress.update_extract_signal.connect(self.update_extract)

    def __show_status_msg(self, msg):
        self.ui.status_bar.showMessage(unicode(msg))

    def finish_walk(self):
        self.flag = False
        self.__show_status_msg(u"分析完成")

    def show_info(self, kv_args):
        file_path = kv_args["file_path"]
        line_num = kv_args["line_num"]
        line = kv_args["line"]
        print "show_info", file_path, line_num, line

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