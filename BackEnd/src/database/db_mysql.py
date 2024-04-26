import pymysql

def get_connection():
    try:
        return pymysql.connect(
            host='localhost',
            database='iot_company',
            user='root',
            passwd=''
)
       
    except Exception as ex: 
        print (ex)