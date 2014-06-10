# coding=UTF-8
from zipfile import ZipFile
import shutil
import os

from progressbar import ProgressBar

from util import spit_filename
from myconfigparser import MyConfigParser


class ExtractFile(object):
    def __init__(self, fp, work_path, regex_util=None, show_info=False, progress=None, eu_text=None):
        self.fp = fp
        self.work_path = work_path
        self.zf = ZipFile(self.fp, mode="r")
        self.regex_util = regex_util
        self.progress = progress
        self.uncompress_size = sum((f.file_size for f in self.zf.infolist()))
        self.show_info = show_info
        self.eu_text = eu_text

    def clean_work_path(self):
        if os.path.exists(self.work_path):
            shutil.rmtree(self.work_path)
        os.mkdir(self.work_path)

    def extract(self):
        members = self.zf.infolist()
        if self.show_info:
            self.start_extract()
        total = 0
        for zip_info in members:
            total += zip_info.file_size
            if not self.regex_util or not self.regex_util.do_match(spit_filename(zip_info.filename, True)):
                if len(zip_info.filename) + len(self.work_path) + 1 < 255:
                    self.zf.extract(zip_info.filename, self.work_path)
                    if self.eu_text and spit_filename(zip_info.filename, True) == "important.properties":
                        file_path = os.path.join(self.work_path, zip_info.filename)
                        cf = MyConfigParser(file_path)
                        regrex = ["\$\{" + key + "\}" for key in cf.keys()]
                        self.eu_text.add_regex(regrex)
                    if self.show_info:
                        self.update_extract(total)
                else:
                    print "path len > 255   ", self.work_path, zip_info.filename
            else:
                pass
        if self.show_info:
            self.finish_extract()
        self.zf.close()

    def start_extract(self):
        if self.progress:
            self.progress.start_extract(fp=self.fp, uncompress_size=self.uncompress_size)

    def finish_extract(self):
        if self.progress:
            self.progress.finish_extract(fp=self.fp)

    def update_extract(self, extract_size):
        if self.progress:
            self.progress.update_extract(extract_size=extract_size)


class IExtractShow(object):
    def __init__(self):
        super(IExtractShow, self).__init__()

    def start_extract(self, **kv_args):
        pass

    def finish_extract(self, **kv_args):
        pass

    def update_extract(self, **kv_args):
        pass


class CliExtractFile(IExtractShow):
    def __init__(self):
        super(CliExtractFile, self).__init__()
        self.pb = None

    def start_extract(self, **kv_args):
        self.pb = ProgressBar(maxval=kv_args["uncompress_size"])
        self.pb.start()

    def finish_extract(self, **kv_args):
        self.pb.finish()

    def update_extract(self, **kv_args):
        self.pb.update(kv_args["extract_size"])





