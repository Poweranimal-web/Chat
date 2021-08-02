from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
query = "UPDATE backupmessage SET status=%s WHERE login=%s AND sender=%s AND status=False"
def change_status3(status,login,sender):
    args = (status,login,sender)
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