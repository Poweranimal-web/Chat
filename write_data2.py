from python_mysql_dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error
query = "INSERT INTO messages(login,message)""VALUES(%s,%s)"
def insert_book1(login, message):
    args = (login, message)
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

