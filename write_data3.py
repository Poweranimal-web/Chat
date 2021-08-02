from python_mysql_dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error
query = "INSERT INTO backupmessage(login,sender,message,status)""VALUES(%s,%s,%s,%s)"
def insert_message4(login,sender,message,status):
    args = (login, sender,message,status)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()