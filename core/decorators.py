# -*- coding: utf-8 -*-
import os
from core.exceptions import FileAccessException


def file_exist_check(func):
    def wrapper(*args, **kwargs):
        file_path, file_name = kwargs["file_path"], kwargs["file_name"]
        if os.access("%s%s" % (file_path, file_name), os.F_OK):
            func(*args, **kwargs)
        else:
            raise FileNotFoundError("File wanted doesn't exist!")
    return wrapper


def file_access_check(func):
    def wrapper(*args, **kwargs):
        file_path, file_name = kwargs["file_path"], kwargs["file_name"]
        if os.access("%s%s" % (file_path, file_name), os.R_OK):
            func(*args, **kwargs)
        else:
            raise FileAccessException(
                "File %s isn't accessible to read!" % file_name
            )
    return wrapper
