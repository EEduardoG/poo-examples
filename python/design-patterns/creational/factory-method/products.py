from abc import ABC, abstractmethod

'''
In this interface, common methods of 
Concrete Products are specified.
'''

class DatabaseProduct(ABC):
    
    @abstractmethod
    def connect():
        pass
    @abstractmethod
    def execute():
        pass
    @abstractmethod
    def disconnect():
        pass


class MySQLConcreteProduct(DatabaseProduct):
    
    def __init__(self):
        self.__host = "localhost"
        self.__dbname = "mysql_database"
        self.__user = "mysql_user"
        self.__password = "passwordmysql"
        self.__driver = "mysql"
        self.__port = "3306"
    
    def connect(self)-> str:
        return {"message": "Connecting to mysql database...", "params": {
            "host": self.__host,
            "dbname": self.__dbname
        }}

    def execute(self)-> str:
        return "Executing query..."

    def disconnect(self)-> str:
        return "Disconnect mysql database..."


class PostgresConcreteProduct(DatabaseProduct):

    def __init__(self):
        self.__host = "localhost"
        self.__dbname = "psql_database"
        self.__user = "psql_user"
        self.__password = "passwordpsql"
        self.__driver = "psql"
        self.__port = "3305"
    
    def connect(self)-> str:
        return {"message": "Connecting to psql database...", "params": {
            "host": self.__host,
            "dbname": self.__dbname
        }}

    def execute(self)-> str:
        return "Executing query..."

    def disconnect(self)-> str:
        return "Disconnect psql database..."


class SQLServerConcreteProduct(DatabaseProduct):
    
    def __init__(self):
        self.__host = "localhost"
        self.__dbname = "tsql_database"
        self.__user = "tsql_user"
        self.__password = "passwordtsql"
        self.__driver = "tsql"
        self.__port = "3304"
      
    def connect(self)-> str:
        return {"message": "Connecting to tsql database...", "params": {
            "host": self.__host,
            "dbname": self.__dbname
        }}

    def execute(self)-> str:
        return "Executing query..."

    def disconnect(self)-> str  :
        return "Disconnect psql database..."