__author__ = 'jervyshi'
from os import walk


def get_all_file(folder=None):
    f = []
    for (dir_path, dir_names, file_names) in walk(folder):
        f.extend(file_names)
        break
    return f
