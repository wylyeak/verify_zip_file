# coding=UTF-8
import codecs
import sys

from PyQt4 import QtGui

from xmlhighlighter import XMLHighlighter


class MyQTextBrowser(QtGui.QTextBrowser):
    def __init__(self, parent=None):
        super(MyQTextBrowser, self).__init__(parent)
        self.fp = None
        self.html_mapper = dict()
        self.highlighter = XMLHighlighter(self.document())

    def select_anchor(self, item):
        if self.fp != item.file_path:
            self.fp = item.file_path
            self.__open_file()

    def __open_file(self):
        html = self.html_mapper.get(self.fp)
        if not html:
            f = codecs.open(self.fp, mode="r", encoding="GB2312")
            html = ""
            for line in f:
                # line = cgi.escape(line)
                # html += "<div>" + line + "</div>"
                html += line
            f.close()
            self.html_mapper[self.fp] = html
        self.setPlainText(html)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = QtGui.QTreeWidget()
    main.text_view = MyQTextBrowser(main)

    class Item:
        def __init__(self):
            self.file_path = None
            self.line_num = None

    item = Item()
    item.file_path = "D:\work\pop-T-order.shop.jd.com-bjshijianwei-ZhengChang-test-r3012_2014-05-27_16.57.37" \
                     "\WEB-INF" \
                     "\lib" \
                     "\pop-vender-order-web-1.1-SNAPSHOT" \
                     "\mongo-config-base.xml"
    item.line_num = 10
    main.text_view.select_anchor(item)
    main.show()
    sys.exit(app.exec_())

