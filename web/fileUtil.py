__author__ = 'jervyshi'
import os
from os import walk


class FileUtil(object):

    @classmethod
    def get_all_file(cls, folder=None):
        f = []
        for (dir_path, dir_names, file_names) in walk(folder):
            f.extend(file_names)
            break
        return f

    @classmethod
    def is_exists(cls, file_name=None):
        return os.path.exists(file_name)

    @classmethod
    def spit_ext(cls, file_name):
        return os.path.basename(file_name).split(".")[-1]

    @classmethod
    def spit_filename(cls, file_name, ext_flag=False):
        if ext_flag:
            return os.path.basename(file_name)
        else:
            basename = os.path.basename(file_name)
            return basename[0:basename.rindex(cls.spit_ext(file_name)) - 1]
