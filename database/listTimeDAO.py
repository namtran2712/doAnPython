from database import connect
import importlib


module = importlib.import_module("database.connect",package="database")

db = module.connector ()

def selectAll ():
    cursor = db.cursor ()
    sql = "SELECT * FROM DEVICE JOIN LISTTIME ON LISTTIME.IDDEVICE = DEVICE.IDDEVICE"
    cursor.execute (sql)
    result = cursor.fetchall ()
    return result