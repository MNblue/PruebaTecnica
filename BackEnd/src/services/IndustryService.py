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


    @classmethod
    def post_Industry(cls, newIndustry: Industry):
        try:
            connection=get_connection()
        
            with connection.cursor() as cursor:
                id_industry = ""
                industry_name = newIndustry.industry_name

                cursor.execute("INSERT INTO industry (id_industry, industry_name )"+
                           "VALUES ('{0}','{1}')".format(id_industry,industry_name))
                
                connection.commit()
                
            
            connection.close()   
            return 'Industria agregada correctamente'
        except Exception as ex: 
            print(ex)


    @classmethod
    def patch_Industry(cls,modifiedIndustry:Industry):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                
                id_industry = modifiedIndustry.id_industry
                industry_name = modifiedIndustry.industry_name
                      
                cursor.execute("UPDATE industry SET industry_name='{1}' WHERE id_industry ='{0}'".format(id_industry, industry_name))                           
                connection.commit()

            connection.close()
            return 'Industria modificada'
        except Exception as ex:  
            print(ex)

    
    @classmethod
    def delete_Industry(cls,id_industry:int):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                             
                cursor.execute("DELETE FROM industry WHERE id_industry='{0}'".format(id_industry))                           
                connection.commit()

            connection.close()
            return 'Industria eliminada'
        except Exception as ex:
            print(ex)


        
    @classmethod
    def search_Industry(cls,id_industry:int):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                             
                cursor.execute("SELECT * FROM industry WHERE id_industry='{0}'".format(id_industry))      
                result = cursor.fetchone()                  
                connection.commit()

            connection.close()
            return result
        except Exception as ex:
            print(ex)