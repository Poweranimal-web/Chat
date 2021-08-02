from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
def get_message(login,sender):
    args = (login,sender)
    messages = {}
    count = 0
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM backupmessage WHERE login=%s AND sender=%s AND status=True",args )
        rows = cursor.fetchall()
        if rows == []:
            return False
        else:
            c = len(rows)
            for row in rows:
                count += 1
                messages['message%s'%count] = row
                if count == c:
                    messages['set'] = 'receive'
                    return messages

    except Error as e:
        print(e)