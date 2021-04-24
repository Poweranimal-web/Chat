from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def delete_book(login):
    db_config = read_db_config()
    args = (login,)
    query = "DELETE FROM messages WHERE login=%s"
    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)

        # execute the query
        cursor = conn.cursor()
        cursor.execute(query, args)

        # accept the change
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

