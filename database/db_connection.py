import mysql.connector
from tables_model import agents, mission

class DB_connection:
    #connect to data base, execute sql, auto conmmit. print exception in case of error and close connection and cursor afterward
    def sql_executer(query:str):
        try:
            connection = mysql.connector.connect()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            connection.close()

    def create_database(self):
        query ="CREATE DATABASE IF NOT EXISTS intelligence-mysql;"
        self.sql_executer(query)

    def get_connection():
        return mysql.connector.connect(
            host= "localhost",
            port= 3306,
            username="intelligence-mysql",
            password=1234,
            database= "Intelligence_db")
        
    def create_tables(self):
        query = agents,mission
        return self.sql_executer(query)
    

