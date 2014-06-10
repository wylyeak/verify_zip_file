# coding=UTF-8
import codecs
import sys

from PyQt4 import QtGui
from PyQt4.Qsci import QsciScintilla, QsciLexerXML
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QFont, QFontMetrics, QColor, QScrollBar


class MyQTextBrowser(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(MyQTextBrowser, self).__init__(parent)
        # Set the default font
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)
        self.setUtf8(True)

        # Margin 0 is used for line numbers
        font_metrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, font_metrics.width("000") + 4)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # Clickable margin 1 for showing markers
        self.setMarginSensitivity(1, True)
        self.connect(self,
                     SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'),
                     self.on_margin_clicked)
        self.markerDefine(QsciScintilla.RightArrow,
                          self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),
                                      self.ARROW_MARKER_NUM)

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4"))

        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #
        lexer = QsciLexerXML()
        lexer.setDefaultFont(font)
        self.setLexer(lexer)
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Courier')

        # Don't want to see the horizontal scrollbar at all
        # Use raw message to Scintilla here (all messages are documented
        # here: http://www.scintilla.org/ScintillaDoc.html)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
        self.setHorizontalScrollBar(QScrollBar(self))

        self.fp = None
        self.item = None
        self.html_mapper = dict()
        self.setReadOnly(True)

    def select_anchor(self, item):
        if self.fp != item.file_path:
            self.fp = item.file_path
            self.item = item
            self.__open_file()
            if item.childCount() == 0:
                parent = item.parent()
            else:
                parent = item
            self.markerDeleteAll()
            for child_item in parent.get_children():
                self.markerAdd(child_item.line_num - 1, self.ARROW_MARKER_NUM)
        self.ensureLineVisible(item.line_num - 1)
        self.setCursorPosition(item.line_num - 1, 0)
        self.ensureCursorVisible()

    def __open_file(self):
        html = self.html_mapper.get(self.fp)
        if not html:
            with codecs.open(self.fp, mode="r", encoding="GB2312") as f:
                html = ""
                for line in f:
                    html += line
            self.html_mapper[self.fp] = html
        self.setText(html)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    editor = MyQTextBrowser()
    editor.show()
    editor.setText(open(sys.argv[0]).read())
    app.exec_()

