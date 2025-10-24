#pip install mysql-connector-python
import mysql.connector

def getConexion():
    try:
        cone = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="concesionaria"
        )
        return cone
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")