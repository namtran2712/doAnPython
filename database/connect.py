import mysql.connector

def connector():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="SMARTHOME"
    )
    return db

