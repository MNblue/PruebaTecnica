from src.database.db_mysql import get_connection
from src.models.deviceModel import Device


class DeviceService():

    @classmethod
    def get_device(cls):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM device')
                result = cursor.fetchall()
                connection.close()
                return result
                   
        except Exception as ex: 
            print(ex)