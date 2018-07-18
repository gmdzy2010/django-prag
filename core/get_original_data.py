import logging
import os
import pandas
import psycopg2
import re


class MethodIllegalException(Exception):
    """Method illegal exception"""
    pass


class BaseDataSource:
    """The base class when dealing with all kinds of data source such as file 
    (txt/csv/tsv/xls/xlsx), database(PostgreSQL, MySQL), stdout(run shell).
    """
    
    data_source_list = []
    data_source_list_add = ""
    _logs_file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs"
    )
    
    def __init__(self, **kwargs):
        """The class instantiation would be done through passing the keyword
        arguments to the instances, the instance variable would be set by the
        function of setattr(obj, key, value)
        """
        self.logger = self.set_logger(self._logs_file_path)
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def dispatch(self, source_kind, **kwargs):
        """This method dispatches specified instance method of getting data to 
        corresponding data source such as "db", by specifying such to argument 
        "source_kind" within the data_source_list, leading to the method of
        "get_data_from_db", to connecting to the data source of database.
        """
        if source_kind.lower() in self.data_source_list:
            method_name = "get_data_from_%s" % source_kind
            handler = getattr(self, method_name, self.method_illegal)
        else:
            handler = self.method_illegal
        return handler(**kwargs)
    
    def update_data_source_list(self):
        if self.data_source_list_add and self.data_source_list:
            self.data_source_list.append(self.data_source_list_add)
        return self.data_source_list
    
    @classmethod
    def get_data_from(cls, source_kind):
        """The first step after class instantiation is to update the variable
        data_source_list through appending data_source_list_add. An empty and
        non-string "source_kind" would raise MethodIllegalException.
        """
        if source_kind and isinstance(source_kind, str):
            source = cls(**DATA_SOURCE[source_kind])
            source.update_data_source_list()
            source.dispatch(source_kind, **DATA_SOURCE[source_kind])
        else:
            raise MethodIllegalException("test exception!")
        
    @property
    def logs_file_path(self):
        """The logs_file_path could only be reset with a effective Unix/Linux
        file path str, and the action of reset would be record in the loggings
        """
        self.logger.info("Logs_file_path: \"%s\"" % self._logs_file_path)
        return self._logs_file_path
    
    @logs_file_path.setter
    def logs_file_path(self, new_path):
        # TODO: to add the file path str of Windows as an effective path
        if isinstance(new_path, str) and re.search(r"/", new_path):
            self._logs_file_path = new_path
            self.logger.warning("New_Logs_file_path: %s" % new_path)
        else:
            self.logger.warning("Failed to reset the logs file path")
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
        

class PostgreSQLDataSource(BaseDataSource):
    """Get the data source for pdf templates from PostgresSQL"""
    data_source_list_add = "db"
    
    def __init__(self, **kwargs):
        super(PostgreSQLDataSource, self).__init__(**kwargs)
    
    def get_data_from_db(self, **kwargs):
        handler = psycopg2.connect(**kwargs)
        cursor = handler.cursor()
        cursor.execute("")
        cursor.commit()
        cursor.close()
    

class MySQLDataSource(BaseDataSource):
    """Get the data source for pdf templates from MySQL"""
    data_source_list_add = "db"
    
    def __init__(self, test, **kwargs):
        self.test = test
        super(MySQLDataSource, self).__init__(**kwargs)
        
    def get_data_from_db(self, **kwargs):
        # TODO #: To replace the package of psycopy2 to the specified package
        handler = psycopg2.connect(**kwargs)
        cursor = handler.cursor()
        cursor.execute("")
        cursor.commit()
        cursor.close()

        
class FileDataSource(BaseDataSource):
    pass


class StdoutDataSource(BaseDataSource):
    pass
    

# if __name__ == "__main__":
#     test = DataSource.dispatch("db")
#     test()
