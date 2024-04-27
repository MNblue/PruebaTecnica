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


    
    
    @classmethod
    def post_wharehouse(cls, newwharehouse: Wharehouse):
        try:
            connection=get_connection()
        
            with connection.cursor() as cursor:
                id_device = newwharehouse.id_device
                id_industry = newwharehouse.id_industry

                cursor.execute("INSERT INTO wharehouse(id_device,id_industry)"+
                           "VALUES ('{0}','{1}')".format(id_device,id_industry))
                
                connection.commit()
                
            
            connection.close()   
            return 'wharehouse agregado correctamente'
        except Exception as ex: 
            print(ex)


    @classmethod
    def patch_wharehouse(cls,wharehouse:Wharehouse,newValue:int):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                
                id_device = wharehouse.id_device
                id_industry = wharehouse.id_industry
                newValue = newValue
                      
                cursor.execute("UPDATE wharehouse SET id_device='{0}', id_industry='{2}' WHERE id_device ={0} and id_industry='{1}'".format(id_device, id_industry,newValue))                           
                connection.commit()

            connection.close()
            return 'wharehouse modificado'
        except Exception as ex:  
            print(ex)

    
    @classmethod
    def delete_wharehouse(cls,id_device:int,id_industry:int):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                             
                cursor.execute("DELETE FROM wharehouse WHERE id_device='{0}' and id_industry='{1}'".format(id_device,id_industry))                           
                connection.commit()

            connection.close()
            return 'wharehouse entrada eliminada'
        except Exception as ex:
            print(ex)


        
