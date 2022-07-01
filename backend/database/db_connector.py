import sqlite3

class DbConnector:
    def __init__(self,dbName):
        self.dbName = dbName

    def get_db_connection(self):
        conn = sqlite3.connect(self.dbName)
        return conn