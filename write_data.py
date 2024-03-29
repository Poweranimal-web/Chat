from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
query = "INSERT INTO users(login,password)""VALUES(%s,%s)"
def insert_book(login, password):
    args = (login, password)
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

if __name__ == '__main__':
    insert_book()
