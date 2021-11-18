from creators import *

class DatabaseFactory():
    @staticmethod
    def get_database(database):
        try:

            if database == "mysql":
                return MySQLConcreteCreator()
            if database == "psql":
                return PostgresConcreteCreator()
            if database == "tsql":
                return SQLServerConcreteCreator()
        
        except AssertionError as _err:
            print(_err)