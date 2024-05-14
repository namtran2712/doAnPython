# from database import connect
# import importlib


# module = importlib.import_module("database.connect",package="database")

# db=module.connector()

# def selectAll ():
#     cursor=db.cursor()
#     sql = "SELECT * FROM DEVICE JOIN PORTDEVICE ON DEVICE.IDDEVICE = PORTDEVICE.IDDEVICE"
#     cursor.execute(sql)
#     result=cursor.fetchall()
#     return result
