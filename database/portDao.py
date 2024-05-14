from database import connect
import importlib

module = importlib.import_module ("database.connect",package="database")

db=module.connector()
def selectByDevice (id):
    sql =f"SELECT portNum FROM portdevice , device WHERE portdevice.idDevice = device.idDevice AND device.idDevice = '{id}'" 
    cursor =db.cursor()
    cursor.execute (sql)
    result = cursor.fetchall ()
    cursor.close ()
    return result

