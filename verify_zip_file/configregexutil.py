# coding=UTF-8
from time import time
import re

from myconfigparser import MyConfigParser


class ConfigRegexUtil(object):
    def __init__(self, cf, section):
        self.cf = cf
        self.section = section
        self.regex_list = list()
        if not cf.get(section):
            cf[section] = {}
        self.__make_regex()

    def add_regex(self, regex):
        key = self.section + "_" + str(int(time()))
        self.cf[self.section][key] = regex
        self.__save_config()
        self.__make_regex()

    def show_items(self):
        for key in self.cf[self.section]:
            value = self.cf[self.section][key]
            print key, value

    def del_regex(self, regex):
        for key in self.cf[self.section]:
            value = self.cf[self.section][key]
            if value == regex:
                del self.cf[self.section][key]
                self.__save_config()
                self.__make_regex()

    def __save_config(self):
        self.cf.write()

    def __make_regex(self):
        line_num = 0
        regex_str = ""
        self.regex_list = list()
        for key in self.cf[self.section]:
            value = self.cf[self.section][key]
            if line_num % 99 == 0:
                if regex_str != "":
                    self.regex_list.insert(line_num // 99, re.compile(regex_str))
                regex_str = "(" + value + ")"
            else:
                regex_str += "|(" + value + ")"
            line_num += 1
        if regex_str != "":
            self.regex_list.insert(line_num // 99, re.compile(regex_str))

    def do_match(self, string):
        for regex in self.regex_list:
            match = regex.match(string)
            if match:
                return True
        return False

    def do_search(self, string):
        for regex in self.regex_list:
            match = regex.search(string)
            if match:
                return match.group()
        return None


if __name__ == "__main__":
    cf = MyConfigParser("config.ini", encoding="UTF-8")

    eu_file = ConfigRegexUtil(cf, "exclude_file")
    eu_text = ConfigRegexUtil(cf, "exclude_txt")
    search_regex = ConfigRegexUtil(cf, "search_regex")

    eu_file.del_regex("^.*\.html$")
    assert False == eu_file.do_match("adfadf.txt.html")
    eu_file.add_regex("^.*\.html$")
    assert True == eu_file.do_match("adfadf.txt.html")

    eu_text.del_regex("^<!--.*-->$")
    assert False == eu_text.do_match("<!--123123123 -->")
    eu_text.add_regex("^<!--.*-->$")
    assert True == eu_text.do_match("<!--123123123 -->")

    assert True == eu_file.do_match("adfadf.txt.html")
    eu_file.del_regex("^.*\.html$")
    assert False == eu_file.do_match("adfadf.txt.html")
    eu_file.add_regex("^.*\.html$")
    assert True == eu_file.do_match("adfadf.txt.html")

    assert True == eu_text.do_match("<!--123123123 -->")
    eu_text.del_regex("^<!--.*-->$")
    assert False == eu_text.do_match("<!--123123123 -->")
    eu_text.add_regex("^<!--.*-->$")
    assert True == eu_text.do_match("<!--123123123 -->")

    search_regex.del_regex("\$\{.+\}")
    assert None == search_regex.do_search('<result name="login" type="redirect">${loginUrl}</result>')
    search_regex.add_regex("\$\{.+\}")
    assert None != search_regex.do_search('<result name="login" type="redirect">${loginUrl}</result>')
    print "test done"