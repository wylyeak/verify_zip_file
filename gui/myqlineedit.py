# coding=UTF-8
from PyQt4 import QtGui


class MyQLineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        super(MyQLineEdit, self).__init__(parent)
        self.clipboard = QtGui.QApplication.clipboard()

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls() or e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            self.setText(unicode(e.mimeData().urls()[0].toLocalFile()))
        else:
            self.setText(unicode(e.mimeData().text()))

    def keyPressEvent(self, q_key_event):
        if q_key_event.matches(QtGui.QKeySequence.Paste):
            if self.clipboard.mimeData().hasUrls():
                self.setText(unicode(self.clipboard.mimeData().urls()[0].toLocalFile()))
            else:
                QtGui.QLineEdit.keyPressEvent(self, q_key_event)
        else:
            QtGui.QLineEdit.keyPressEvent(self, q_key_event)
