from factory import *

if __name__ == "__main__":
    
    CONNECT = DatabaseFactory.get_database('tsql').instance().connect()
    EXECUTE = DatabaseFactory.get_database('tsql').instance().execute()
    DISSCONECT = DatabaseFactory.get_database('tsql').instance().disconnect()
    
    print(CONNECT)
    print(EXECUTE)
    print(DISSCONECT)

