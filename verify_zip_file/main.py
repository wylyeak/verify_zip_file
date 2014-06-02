# coding=UTF-8
import sys

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_main_window


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setAcceptDrops(True)

    def paste_file(self):
        if self.clipboard.mimeData().hasUrls():
            self.__set_zip_path(self.clipboard.mimeData().urls()[0].toLocalFile())

    def __set_zip_path(self, url):
        self.ui.zip_path.setText(unicode(url))

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def __set_status_msg(self, msg):
        self.status_bar.showMessage(unicode(msg))

    def dropEvent(self, e):
        self.__set_zip_path(e.mimeData().urls()[0].toLocalFile())

        # def __start_verify(self):
        #     if os.path.isfile(str(self.zip_path.text())):
        #         vf = VerifyFile(str(self.zip_path.text()), str(self.work_path.text()), "config.ini", True)
        #         vf.walk()
        #     else:
        #         print "path is"
        #         pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())