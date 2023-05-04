import mysql.connector
import sys
def connect():
    mydb = mysql.connector.connect(
        host ='localhost',
        database = 'test',
        user = 'root',
        password = '',
    )
    try:
        connect_obj = mydb.cursor()
        name ='alen'
        sex = 'male'
        Qu = """insert into data (name,sex) values('als','maless')"""
        connect_obj.execute(Qu)
        status = mydb.commit()
        print(status)
        return True
    except :
        print('error :',sys.exc_info()[0])

print(connect())