# coding=UTF-8
from zipfile import ZipFile
import shutil
import os

from progressbar import ProgressBar

from util import spit_filename


class ExtractFile(object):
    def __init__(self, fp, work_path, regex_util=None, show_info=False):
        self.fp = fp
        self.work_path = work_path
        self.zf = ZipFile(self.fp, mode="r")
        self.regex_util = regex_util
        self.uncompress_size = sum((f.file_size for f in self.zf.infolist()))
        self.show_info = show_info

    def clean_work_path(self):
        if os.path.exists(self.work_path):
            shutil.rmtree(self.work_path)
        os.mkdir(self.work_path)

    def extract(self):
        members = self.zf.infolist()
        if self.show_info:
            self.start_extract()
            # pb = ProgressBar(maxval=self.uncompress_size)
            # pb.start()
        total = 0
        for zip_info in members:
            total += zip_info.file_size
            if not self.regex_util or not self.regex_util.do_match(spit_filename(zip_info.filename, True)):
                if len(zip_info.filename) + len(self.work_path) + 1 < 255:
                    self.zf.extract(zip_info.filename, self.work_path)
                    if self.show_info:
                        self.update_extract(total)
                        # pb.update(total)
                else:
                    print "path len > 255   ", self.work_path, zip_info.filename
            else:
                pass
                # print zip_info.filename
        if self.show_info:
            self.finish_extract()
        self.zf.close()

    def start_extract(self):
        pass

    def finish_extract(self):
        pass

    def update_extract(self, extract_size):
        pass


class CliExtractFile(ExtractFile):
    def __init__(self, fp, work_path, regex_util=None, show_info=False):
        super(CliExtractFile, self).__init__(fp, work_path, regex_util, show_info)
        self.pb = None

    def start_extract(self):
        self.pb = ProgressBar(maxval=self.uncompress_size)
        self.pb.start()

    def finish_extract(self):
        self.pb.finish()

    def update_extract(self, extract_size):
        self.pb.update(extract_size)





