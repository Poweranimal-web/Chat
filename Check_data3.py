from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
def query_with_fetchall(login):
    args = (login,)
    messages = {}
    count = 0
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages WHERE login=%s" ,args )
        rows = cursor.fetchall()
        if rows == []:
            messages['set'] = 'no'
            return messages
        else:
            c = len(rows)
            for row in rows:
                count += 1
                messages['message%s'%count] = row
                if count == c:
                    messages['set'] = 'GET'
                    return messages

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
if __name__ == '__main__':
    query_with_fetchall()