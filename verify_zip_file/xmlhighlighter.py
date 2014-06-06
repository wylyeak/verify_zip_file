# coding=UTF-8

from PyQt4 import QtGui, QtCore


class XMLHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(XMLHighlighter, self).__init__(parent)

        keyword_format = QtGui.QTextCharFormat()
        keyword_format.setForeground(QtCore.Qt.darkMagenta)
        keyword_format.setFontWeight(QtGui.QFont.Bold)

        keyword_patterns = ["\\b?xml\\b", "/>", ">", "<"]

        self.highlighting_rules = [(QtCore.QRegExp(pattern), keyword_format)
                                   for pattern in keyword_patterns]

        xml_element_format = QtGui.QTextCharFormat()
        xml_element_format.setFontWeight(QtGui.QFont.Bold)
        xml_element_format.setForeground(QtCore.Qt.blue)
        self.highlighting_rules.append((QtCore.QRegExp("\\b[A-Za-z0-9_-]+(?=[\s/>])"), xml_element_format))

        xml_attribute_format = QtGui.QTextCharFormat()
        xml_attribute_format.setFontItalic(True)
        xml_attribute_format.setForeground(QtCore.Qt.red)
        self.highlighting_rules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\=)"), xml_attribute_format))

        self.value_format = QtGui.QTextCharFormat()
        self.value_format.setForeground(QtCore.Qt.darkBlue)

        self.value_start_expression = QtCore.QRegExp("\"")
        self.value_end_expression = QtCore.QRegExp("\"(?=[\s></])")

        single_line_comment_format = QtGui.QTextCharFormat()
        single_line_comment_format.setForeground(QtCore.Qt.gray)
        self.highlighting_rules.append((QtCore.QRegExp("<!--\s*[^#]*\s*-->"), single_line_comment_format))

    def highlightBlock(self, text):
        #----------------------
        expression = QtCore.QRegExp("^.+$")
        line_num = 1
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            line_num_format = QtGui.QTextCharFormat()
            line_num_format.setAnchor(True)
            line_num_format.setAnchorHref("#page_" + str(line_num))
            line_num_format.setAnchorName("#page_" + str(line_num))
            self.setFormat(index, length, line_num_format)
            index = expression.indexIn(text, index + length)
            line_num += 1
        #----------------------

        #for every pattern
        for pattern, _format in self.highlighting_rules:
            expression = QtCore.QRegExp(pattern)

            index = expression.indexIn(text)

            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, _format)

                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        start_index = 0
        if self.previousBlockState() != 1:
            start_index = self.value_start_expression.indexIn(text)

        while start_index >= 0:
            end_index = self.value_end_expression.indexIn(text, start_index)

            if end_index == -1:
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_index
            else:
                comment_length = end_index - start_index + self.value_end_expression.matchedLength()

            self.setFormat(start_index, comment_length, self.value_format)

            start_index = self.value_start_expression.indexIn(text, start_index + comment_length)

