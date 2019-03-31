import pymysql

from config import *

def connection_mysql():
    conn = None
    try:
        conn = pymysql.connect(user=user_mysql, passwd=password_mysql, host=host, port=3306, db=database)
    except ConnectionRefusedError as e:
        conn = None
        print(e.__context__)
    except pymysql.err.OperationalError as e:
        conn = None
        print(e.__context__)
    except Exception as e:
        conn = None
        print(e.__context__)
    return conn 