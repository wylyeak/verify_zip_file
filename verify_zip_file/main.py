# coding=UTF-8
import sys

from PyQt4 import QtGui

from mainwindow import Ui_main_window


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.work_path.setText(unicode("D:\\work"))

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