from database import connect
import importlib


module = importlib.import_module("database.connect",package="database")

db=module.connector()
def selectAll():
    cursor=db.cursor()

    sql="Select * from user"
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

def delete(id):
    cursor=db.cursor()
    sql=f"Delete from user where idUser={id}"
    cursor.execute(sql)
    db.commit ()

def insert(name, birthday, phone, username, pw):
    if (getUserByPhoneorUsername (phone,username)):
        return False
    cursor=db.cursor()
    sql=f"Insert into user(nameUser,dateUser,phoneUser, Username,Password) Values('{name}','{birthday}','{phone}','{username}','{pw}')"
    cursor.execute(sql)
    db.commit ()
    return True
def update(name, birthday, phone,id):
    
    cursor=db.cursor()
    sql=f"Update user Set nameUser='{name}',dateUser='{birthday}',phoneUser='{phone}' Where idUser={id}"
    print (sql)
    cursor.execute(sql)
    db.commit()
    return True

def selectByUsername (username, pw):
    cursor=db.cursor()
    sql= "SELECT * ".join (
        "FROM USER ".join (
            f"WHERE Username = {username} and Password = {pw}" 
        )
    )
    sql = f"select * from user where Username = '{username}' and Password = '{pw}'"
    cursor.execute(sql)
    result = cursor.fetchall ()
    return len(result)

def selectByID (id):
    cursor=db.cursor()
    sql = f"select * from user where idUser = {id}"
    print (sql)
    cursor.execute(sql)
    result = cursor.fetchall ()
    return result

def getLastId ():
    sql ="select * from user order by idUser desc limit 1"
    cursor =db.cursor ()
    cursor.execute (sql)
    result =cursor.fetchall ()
    return result

def getUserByPhoneorUsername (phone,username):
    sql =f"select * from user where phoneUser ='{phone} 'or Username='{username}' "
    cursor =db.cursor ()
    cursor.execute (sql)
    result =cursor.fetchall ()
    return len(result) >0

def checkMatchPhone (phone ,id):
    sql =f"select * from user where phoneUser ='{phone}' and idUser <> {id}"
    cursor =db.cursor ()
    cursor.execute (sql)
    result =cursor.fetchall ()
    return len(result) > 0