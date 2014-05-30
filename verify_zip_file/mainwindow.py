# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri May 30 16:17:04 2014
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
        main_window.resize(640, 480)
        main_window.setMinimumSize(QtCore.QSize(640, 480))
        main_window.setMouseTracking(False)
        main_window.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 11, 616, 421))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontal_layout = QtGui.QHBoxLayout()
        self.horizontal_layout.setObjectName(_fromUtf8("horizontal_layout"))
        self.zip_path_label = QtGui.QLabel(self.widget)
        self.zip_path_label.setObjectName(_fromUtf8("zip_path_label"))
        self.horizontal_layout.addWidget(self.zip_path_label)
        self.zip_path = QtGui.QLineEdit(self.widget)
        self.zip_path.setMinimumSize(QtCore.QSize(471, 0))
        self.zip_path.setObjectName(_fromUtf8("zip_path"))
        self.horizontal_layout.addWidget(self.zip_path)
        self.config_path = QtGui.QLabel(self.widget)
        self.config_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.config_path.setObjectName(_fromUtf8("config_path"))
        self.horizontal_layout.addWidget(self.config_path)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.horizontal_layout_2 = QtGui.QHBoxLayout()
        self.horizontal_layout_2.setObjectName(_fromUtf8("horizontal_layout_2"))
        self.work_path_label = QtGui.QLabel(self.widget)
        self.work_path_label.setObjectName(_fromUtf8("work_path_label"))
        self.horizontal_layout_2.addWidget(self.work_path_label)
        self.work_path = QtGui.QLineEdit(self.widget)
        self.work_path.setMinimumSize(QtCore.QSize(471, 0))
        self.work_path.setObjectName(_fromUtf8("work_path"))
        self.horizontal_layout_2.addWidget(self.work_path)
        self.start_button = QtGui.QPushButton(self.widget)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontal_layout_2.addWidget(self.start_button)
        self.verticalLayout.addLayout(self.horizontal_layout_2)
        self.splitter = QtGui.QSplitter(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tree_view = QtGui.QTreeView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_view.sizePolicy().hasHeightForWidth())
        self.tree_view.setSizePolicy(sizePolicy)
        self.tree_view.setObjectName(_fromUtf8("tree_view"))
        self.text_view = QtGui.QTextBrowser(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_view.sizePolicy().hasHeightForWidth())
        self.text_view.setSizePolicy(sizePolicy)
        self.text_view.setObjectName(_fromUtf8("text_view"))
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout.setStretch(2, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menu_bar = QtGui.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.menu = QtGui.QMenu(self.menu_bar)
        self.menu.setObjectName(_fromUtf8("menu"))
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QtGui.QStatusBar(main_window)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        main_window.setStatusBar(self.status_bar)
        self.paste_action = QtGui.QAction(main_window)
        self.paste_action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.paste_action.setObjectName(_fromUtf8("paste_action"))
        self.quit_action = QtGui.QAction(main_window)
        self.quit_action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.quit_action.setObjectName(_fromUtf8("quit_action"))
        self.menu.addAction(self.paste_action)
        self.menu.addSeparator()
        self.menu.addAction(self.quit_action)
        self.menu_bar.addAction(self.menu.menuAction())

        self.retranslateUi(main_window)
        QtCore.QObject.connect(self.quit_action, QtCore.SIGNAL(_fromUtf8("triggered()")), main_window.close)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "验证工具", None))
        self.zip_path_label.setText(_translate("main_window", "Zip Path:", None))
        self.config_path.setText(_translate("main_window", "选择config", None))
        self.work_path_label.setText(_translate("main_window", "WorkPath:", None))
        self.start_button.setText(_translate("main_window", "Start", None))
        self.menu.setTitle(_translate("main_window", "文件", None))
        self.paste_action.setText(_translate("main_window", "粘贴", None))
        self.paste_action.setShortcut(_translate("main_window", "Ctrl+V", None))
        self.quit_action.setText(_translate("main_window", "退出", None))
        self.quit_action.setShortcut(_translate("main_window", "Ctrl+Q", None))

