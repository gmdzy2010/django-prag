import logging
import os
import pandas
import psycopg2
# from .decorators import *
# from .exceptions import *


DATA_SOURCE = {
    "db": {
        "host": "192.168.0.100",
        "port": 5432,
        "database": "colowell",
        "user": "postgres",
        "password": "postgres",
    },
    "file": {
        "path": "/usr/bin/",
    },
    "stdout": {
        "info": "This function hadn't been developed, please wait for updating"
                "in next version",
        "command": "ps aux|grep test",
    },
}


class MethodIllegalException(Exception):
    """
    Method illegal exception
    """
    pass


class BaseDataSource:
    """
    The base class when dealing with all kinds of data source
    """
    data_source_list = []
    data_source_list_add = ""
    _logs_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs"
    )
    
    def __init__(self, **kwargs):
        self.logger = self.set_logger(self._logs_path)
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def dispatch(self, source_kind, **kwargs):
        # The argument "source_kind" would be transformed to lowercase
        # and it should have been contained within the data_source_list
        if source_kind.lower() in self.data_source_list:
            method_name = "get_data_from_%s" % source_kind
            handler = getattr(self, method_name, self.method_illegal)
        else:
            handler = self.method_illegal
        return handler(**kwargs)
    
    def refresh_data_source_list(self):
        # The first step after class instantiation is to update the 
        # data_source_list through appending data_source_list_add
        if self.data_source_list_add and self.data_source_list:
            self.data_source_list.append(self.data_source_list_add)
        return self.data_source_list
    
    @classmethod
    def get_data_from(cls, source_kind):
        if source_kind and isinstance(source_kind, str):
            source = cls(**DATA_SOURCE[source_kind])
            source.refresh_data_source_list()
            source.dispatch(source_kind, **DATA_SOURCE[source_kind])
        else:
            raise MethodIllegalException("test exception!")
        
    @property
    def logs_path(self):
        return self._logs_path
    
    @logs_path.setter
    def logs_path(self, new_path):
        if isinstance(new_path, str):
            self._logs_path = new_path
        else:
            self.logger.info("Failed to reset the logs file path")
            raise ValueError("Illegal value of logs file path, Must be a str!")
    
    def set_logger(self, logs_path):
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)
        logger_file = os.path.join(logs_path, '%s.info' % __name__)
        logger_handler = logging.FileHandler(logger_file)
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logger_handler.setFormatter(logger_formatter)
        logger.addHandler(logger_handler)
        return logger

    def store_data(self):
        pass
    
    def method_illegal(self, **kwargs):
        pass
        


