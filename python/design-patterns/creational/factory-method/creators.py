
from products import *

class DatabaseCreator(ABC):
    @abstractmethod
    def instance(self):
        pass

class MySQLConcreteCreator(DatabaseCreator):
    def instance(self) -> DatabaseProduct:
        return MySQLConcreteProduct()

class PostgresConcreteCreator(DatabaseCreator):
    def instance(self) -> DatabaseProduct:
        return PostgresConcreteProduct()

class SQLServerConcreteCreator(DatabaseCreator):
    def instance(self) -> DatabaseProduct:
        return SQLServerConcreteProduct()