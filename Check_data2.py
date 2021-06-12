from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def query_with_fetchone(login):
    args = (login,)
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages WHERE login=%s" ,args)

        row = cursor.fetchone()

        if row is not None:
            return row
        else:
            return False

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
