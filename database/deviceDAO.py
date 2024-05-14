from database import connect
import importlib

module = importlib.import_module("database.connect", package="database")
db = module.connector()


def selectAll():
    sql = "select * from device"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result
def selectDeviceById (id):
    sql =f"select * from device , portdevice where device.idDevice =  portdevice.idDevice and device.idDevice= {id} "
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result
def getLastIdDevice ():
    sql = "select * from device order by idDevice desc limit 1"
    cursor = db.cursor()
    cursor.execute(sql)
    result  =cursor.fetchall ()
    return result[0][0]
def insertDevice(nameDevice, typeDevice, location ,listport ):
    sql = f"INSERT INTO device (nameDevice,typeDevice,position) VALUES ('{nameDevice}' , '{typeDevice}' , '{location}')"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    id =getLastIdDevice()
    for port in listport :
        sql =f"INSERT INTO portdevice (portNum,idDevice) VALUES ({int (port)} ,  { int (id)}) "
        cursor.execute(sql)
        db.commit()
    cursor.close()
def deleteDevice (id):
    sql =f"delete from device where device.idDevice = {id} "
    cursor=db.cursor ()
    cursor.execute (sql)
    db.commit ()
    cursor.close ()
def update (id,nameDevice, typeDevice, location ,listport ):
    sql =f"update device set idDevice={id}, nameDevice ='{nameDevice}',position ='{location}',typeDevice ='{typeDevice}' where idDevice ={id}"
    cursor=db.cursor ()
    cursor.execute (sql)
    db.commit ()
    
    sql =f"delete from portdevice where portdevice.idDevice={id}"
    cursor.execute (sql)
    db.commit ()

    for port in listport :
        sql =f"INSERT INTO portdevice (portNum,idDevice) VALUES ({int (port)} ,  { int (id)}) "
        cursor.execute(sql)
        db.commit()
    cursor.close ()
       


