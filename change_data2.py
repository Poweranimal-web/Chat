from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
query = "UPDATE backupmessage SET status=%s WHERE sender=%s  AND status=True"
def change_status(status,sender):
    args = (status,sender)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()