# coding=UTF-8
import os


def spit_ext(file_name):
    return os.path.basename(file_name).split(".")[-1]


def spit_filename(file_name, ext_flag=False):
    file_name = os.path.normpath(str(file_name))
    if ext_flag:
        return os.path.basename(file_name)
    else:
        basename = os.path.basename(file_name)
        return basename[0:basename.rindex(spit_ext(file_name)) - 1]


def parse_bool(bool_str):
    if not bool_str:
        return False
    return bool_str.lower() == "true"

