# 3. Demonstrate abstraction by:
#   - Creating an abstract class `Database`
#   - Implementing `connect()` in `MySQLDatabase` and `PostgresDatabase`

from abc import ABC, abstractmethod
import math 

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
class MySQLDatabase(Database):
    def connect(self):
        return "MySQL is connected"
        
class PostgresDatabase(Database):
    def connect(self):
        return "Postgres is connected"
        
        
s1 = MySQLDatabase()
p1 = PostgresDatabase()

print(s1.connect())
print(p1.connect())
        
