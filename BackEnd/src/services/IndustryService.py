from src.database.db_mysql import get_connection
from src.models.industryModel import Industry


class IndustryService():

    @classmethod
    def get_Industry(cls):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM industry')
                result = cursor.fetchall()
                connection.close()
                return result
                   
        except Exception as ex: 
            print(ex)