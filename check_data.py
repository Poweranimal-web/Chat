from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
def query_with_fetchone(login,password):
    args = (login,password)
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login=%s AND password=%s",args)
        row = cursor.fetchone()
        if row is not cursor.fetchone():
            return True
        else:
            return False
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

