# coding=UTF-8
from PyQt4 import QtGui


class MyQTreeWidget(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        super(MyQTreeWidget, self).__init__(parent)