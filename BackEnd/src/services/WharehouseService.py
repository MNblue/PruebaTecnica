from src.database.db_mysql import get_connection
from src.models.wharehouseModel import Wharehouse


class WharehouseService():

    @classmethod
    def get_wharehouse(cls):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM wharehouse')
                result = cursor.fetchall()
                connection.close()
                return result
                   
        except Exception as ex: 
            print(ex)