from src.database.db_mysql import get_connection
from src.models.deviceModel import Device
from datetime import datetime


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


    
    @classmethod
    def post_device(cls, newdevice: Device):
        try:
            connection=get_connection()
        
            with connection.cursor() as cursor:
                id_device = ""
                device_name = newdevice.device_name
                fecha_actual = datetime.now()
                date_format = fecha_actual.strftime("%Y-%m-%d")
                addition_time = date_format
                fee = newdevice.fee

                cursor.execute("INSERT INTO device(id_device,device_name,addition_time,fee)"+
                           "VALUES ('{0}','{1}','{2}','{3}')".format(id_device,device_name,addition_time,fee))
                
                connection.commit()
                
            
            connection.close()   
            return 'Dispositivo agregado correctamente'
        except Exception as ex: 
            print(ex)


    @classmethod
    def patch_device(cls,modifiedDevice:Device):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                
                id_device = modifiedDevice.id_device
                device_name = modifiedDevice.device_name
                fee = modifiedDevice.fee
                      
                cursor.execute("UPDATE device SET device_name='{1}', fee='{2}' WHERE id_device ={0}".format(id_device, device_name,fee))                           
                connection.commit()

            connection.close()
            return 'Dispositivo modificado'
        except Exception as ex:  
            print(ex)

    
    @classmethod
    def delete_Device(cls,id_device:int):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                             
                cursor.execute("DELETE FROM device WHERE id_device='{0}'".format(id_device))                           
                connection.commit()

            connection.close()
            return 'Dispositivo eliminado'
        except Exception as ex:
            print(ex)


        
    @classmethod
    def search_device(cls,id_device:int):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                             
                cursor.execute("SELECT * FROM device WHERE id_device='{0}'".format(id_device))      
                result = cursor.fetchone()                  
                connection.commit()

            connection.close()
            return result
        except Exception as ex:
            print(ex)