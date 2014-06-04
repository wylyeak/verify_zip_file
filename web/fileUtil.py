__author__ = 'jervyshi'
from os import walk


class FileUtil(object):

    @classmethod
    def get_all_file(cls, folder=None):
        f = []
        for (dir_path, dir_names, file_names) in walk(folder):
            f.extend(file_names)
            break
        return f
