from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def find_friend(login):
    args = (login,)
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login=%s", args)
        row = cursor.fetchone()

        while row is not None:
            return True
        else:
            return False

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

