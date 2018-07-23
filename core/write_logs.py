# -*- coding: utf-8 -*-
import logging
import os
import re
from conf.configurations import LOGGING_FILE_PATH

class LoggingRecorder:
    """the package logging recoder"""
    _logs_file_path = LOGGING_FILE_PATH
    
    @classmethod
    def get_logger(cls, logs_file_name):
        logger = logging.getLogger(__name__)
        logger_file = os.path.join(cls._logs_file_path, logs_file_name)
        logger_handler = logging.FileHandler(logger_file)
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter(
            "[%(asctime)s/%(name)s/%(levelname)s/%(message)s]"
        )
        logger_handler.setFormatter(logger_formatter)
        logger.addHandler(logger_handler)
        return logger
    
    @property
    def logs_file_path(self):
        """The logs_file_path could only be reset with a effective Unix/Linux
        file path str, and the action of reset would be recorded in log file.
        """
        return self._logs_file_path
    
    @logs_file_path.setter
    def logs_file_path(self, new_path):
        # TODO: to add the file path str of Windows as an effective path
        if isinstance(new_path, str) and re.search(r'/', new_path):
            self._logs_file_path = new_path
        else:
            raise ValueError("Illegal value of logs file path, Must be a str!")
