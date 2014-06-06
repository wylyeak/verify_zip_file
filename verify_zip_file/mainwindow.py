# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jun 06 15:53:07 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.setWindowModality(QtCore.Qt.ApplicationModal)
        main_window.resize(640, 518)
        main_window.setMinimumSize(QtCore.QSize(640, 480))
        main_window.setMouseTracking(False)
        main_window.setAcceptDrops(False)
        self.central_widget = QtGui.QWidget(main_window)
        self.central_widget.setAcceptDrops(False)
        self.central_widget.setObjectName(_fromUtf8("central_widget"))
        self.gridLayout = QtGui.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vertical_layout = QtGui.QVBoxLayout()
        self.vertical_layout.setObjectName(_fromUtf8("vertical_layout"))
        self.horizontal_layout = QtGui.QHBoxLayout()
        self.horizontal_layout.setObjectName(_fromUtf8("horizontal_layout"))
        self.zip_path_label = QtGui.QLabel(self.central_widget)
        self.zip_path_label.setObjectName(_fromUtf8("zip_path_label"))
        self.horizontal_layout.addWidget(self.zip_path_label)
        self.zip_path = MyQLineEdit(self.central_widget)
        self.zip_path.setMinimumSize(QtCore.QSize(471, 0))
        self.zip_path.setAcceptDrops(True)
        self.zip_path.setObjectName(_fromUtf8("zip_path"))
        self.horizontal_layout.addWidget(self.zip_path)
        self.config_path = QtGui.QPushButton(self.central_widget)
        self.config_path.setAcceptDrops(False)
        self.config_path.setObjectName(_fromUtf8("config_path"))
        self.horizontal_layout.addWidget(self.config_path)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.horizontal_layout_2 = QtGui.QHBoxLayout()
        self.horizontal_layout_2.setObjectName(_fromUtf8("horizontal_layout_2"))
        self.work_path_label = QtGui.QLabel(self.central_widget)
        self.work_path_label.setObjectName(_fromUtf8("work_path_label"))
        self.horizontal_layout_2.addWidget(self.work_path_label)
        self.work_path = MyQLineEdit(self.central_widget)
        self.work_path.setMinimumSize(QtCore.QSize(471, 0))
        self.work_path.setAcceptDrops(True)
        self.work_path.setObjectName(_fromUtf8("work_path"))
        self.horizontal_layout_2.addWidget(self.work_path)
        self.start_button = QtGui.QPushButton(self.central_widget)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontal_layout_2.addWidget(self.start_button)
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        self.splitter = QtGui.QSplitter(self.central_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tree_view = MyQTreeWidget(self.splitter)
        self.tree_view.setEnabled(True)
        self.tree_view.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tree_view.setObjectName(_fromUtf8("tree_view"))
        self.text_view = MyQTextBrowser(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_view.sizePolicy().hasHeightForWidth())
        self.text_view.setSizePolicy(sizePolicy)
        self.text_view.setAcceptDrops(False)
        self.text_view.setObjectName(_fromUtf8("text_view"))
        self.vertical_layout.addWidget(self.splitter)
        self.progress_bar = QtGui.QProgressBar(self.central_widget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.vertical_layout.addWidget(self.progress_bar)
        self.gridLayout.addLayout(self.vertical_layout, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.status_bar = QtGui.QStatusBar(main_window)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        main_window.setStatusBar(self.status_bar)
        self.menuBar = QtGui.QMenuBar(main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        main_window.setMenuBar(self.menuBar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "验证工具", None))
        self.zip_path_label.setText(_translate("main_window", "Zip Path:", None))
        self.config_path.setText(_translate("main_window", "选择config", None))
        self.work_path_label.setText(_translate("main_window", "WorkPath:", None))
        self.start_button.setText(_translate("main_window", "Start", None))
        self.tree_view.headerItem().setText(0, _translate("main_window", "文件", None))
        self.tree_view.headerItem().setText(1, _translate("main_window", "行号", None))

from myqtextbrowser import MyQTextBrowser
from myqlineedit import MyQLineEdit
from myqtreewidget import MyQTreeWidget
