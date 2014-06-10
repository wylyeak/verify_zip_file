#!/usr/bin/python
# coding=UTF-8

import os
import sys

from configregexutil import ConfigRegexUtil
from extractutil import ExtractFile, CliExtractFile
from util import spit_filename, spit_ext, parse_bool
from myconfigparser import MyConfigParser


class VerifyFile(object):
    def __init__(self, zip_file_path, work_path, config_path, show_extract_progress=False, analyze_info=None,
                 extract_progress=None):
        self.zip_file_path = zip_file_path
        self.work_path = work_path + os.sep + spit_filename(zip_file_path) + os.sep
        self.show_extract_progress = show_extract_progress
        self.is_extract_root = False
        self.extract_progress = extract_progress
        self.analyze_info = analyze_info
        self.cf = MyConfigParser(config_path, encoding="UTF-8")
        self.eu_file = ConfigRegexUtil(self.cf, "exclude_file")
        self.eu_text = ConfigRegexUtil(self.cf, "exclude_txt")
        self.search_regex = ConfigRegexUtil(self.cf, "search_regex")

    def __extract_root(self):
        root_ef = self.make_extract(self.zip_file_path, self.work_path)
        root_ef.clean_work_path()
        root_ef.extract()

    def analyze_file(self, file_path):
        with open(file_path) as f:
            line_num = 0
            for line in f:
                line = line.strip()
                line_num += 1
                if not self.eu_text.do_match(line):
                    res = self.search_regex.do_search(line)
                    if res and not self.eu_text.do_match(res):
                        self.show_info(file_path=file_path, line_num=line_num, line=line, matcher=res)

    def show_info(self, file_path, line_num, line, matcher):
        if self.analyze_info:
            self.analyze_info.show_info(file_path=file_path,
                                        relative_file_path=file_path[len(self.work_path): len(file_path)],
                                        line_num=line_num, line=line, matcher=matcher)
        else:
            print file_path, line_num, line, matcher

    def walk(self):
        self.__walk(self.work_path)
        if self.analyze_info:
            self.analyze_info.finish_verify(fp=self.zip_file_path)

    def make_extract(self, zip_file_path, work_path):
        return ExtractFile(zip_file_path, work_path, self.eu_file, self.show_extract_progress, self.extract_progress,
                           eu_text=self.eu_text)

    def __walk(self, file_path):
        if not self.is_extract_root:
            self.is_extract_root = True
            self.__extract_root()
        walk_res = os.walk(file_path)
        for dir_path, dir_names, file_names in walk_res:
            for file_name in file_names:
                abs_file_path = os.path.join(dir_path, file_name)
                ext = spit_ext(abs_file_path)
                if ext == "jar":
                    if not self.eu_file.do_match(file_name):
                        jar_extract_path = dir_path + os.sep + spit_filename(file_name)
                        ef = self.make_extract(abs_file_path, jar_extract_path)
                        ef.clean_work_path()
                        ef.extract()
                        self.__walk(jar_extract_path)
                else:
                    if not self.eu_file.do_match(file_name):
                        self.analyze_file(abs_file_path)


class IVerifyFileShow(object):
    def __init__(self):
        super(IVerifyFileShow, self).__init__()

    def show_info(self, **kv_args):
        pass

    def finish_verify(self, **kv_args):
        pass


if __name__ == "__main__":
    if len(sys.argv) == 5:
        zipfile = sys.argv[1]
        path = sys.argv[2]
        cfg_name = sys.argv[3]
        vf = VerifyFile(zipfile, path, cfg_name, parse_bool(sys.argv[4]), extract_progress=CliExtractFile())
        vf.walk()
    else:
        print "param1: zip_path", "param2: extract_path", "param3:config.ini path",
        print "param4: show_extract_progress( True || False)"
        exit(1)


