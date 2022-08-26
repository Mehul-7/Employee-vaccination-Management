from sqlite3 import DatabaseError
import mysql.connector


class DbConnection:
    my_db=None
    _instance=None
    @staticmethod
    def get_instance():
        if DbConnection.my_db is None:
            DbConnection()
        return DbConnection.my_db

    def __init__(self):
        if DbConnection.my_db is None:
            DbConnection.my_db=mysql.connector.connect(
                host="localhost",
                user="mehul",
                passwd="9@$$Mehul",
                database="vaccination"
            )
            DbConnection._instance=self
            
            
                


