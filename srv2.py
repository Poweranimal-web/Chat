import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
from write_data import insert_book
from check_data import query_with_fetchone1
from write_data2 import insert_book1
from Check_data2 import query_with_fetchone
from delete_data import delete_book
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
port = 9090

class Chat(Protocol):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = addr
    def connectionMade(self):
       self.factory.numProtocols =+1
       hi = {}
       hi['set'] = 'Hello from server'
       a = json.dumps(hi)
       self.transport.write(a.encode('utf-8'))
    def dataReceived(self, data):
        d = data.decode('utf-8')
        struc = json.loads(d)
        if struc['set'] == 'auth':
            del struc['set']
            login = struc['login']
            password = struc['password']
            a = query_with_fetchone1(login, password)
            auth = {}
            auth['set'] = 'auth'
            b = json.dumps(auth)
            no_auth = {}
            no_auth['set'] = 'no auth'
            c = json.dumps(no_auth)
            if a == True:
                self.transport.write(b.encode('utf-8'))
            else:
                self.transport.write(c.encode('utf-8'))
        elif struc['set'] == 'registr':
            del struc['set']
            login = struc['login']
            password = struc['password']
            insert_book(login, password)
            auth = {}
            auth['set'] = 'auth'
            b = json.dumps(auth)
            self.transport.write(b.encode('utf-8'))
        elif struc['set'] == 'write message':
            del struc['set']
            message = "{}:{}".format(struc['sender'], struc['message'])
            c = struc['receipient']
            insert_book1(c, message)
            bring = {}
            bring['set'] = 'bring'
            a = json.dumps(bring)
            self.transport.write(a.encode('utf-8'))
        elif struc['set'] == 'Get':
            del struc['set']
            login = struc['nick']
            mesg = {}
            b = query_with_fetchone(login)
            mesg['set'] = 'GET'
            mesg['mesg'] = b
            cr = json.dumps(mesg)
            delete_book(login)
            if b == False:
                no_mesg = {}
                no_mesg['set'] = 'no mesg'
                a = json.dumps(no_mesg)
                self.transport.write(a.encode('utf-8'))
            else:
                self.transport.write(cr.encode('utf-8'))
        elif struc['set'] == 'GET USERS':
            try:
                dbconfig = read_db_config()
                conn = MySQLConnection(**dbconfig)
                cursor = conn.cursor()
                cursor.execute("SELECT login FROM users")
                rows = cursor.fetchall()
                users = []

                for row in rows:
                    users.append(row)


            except Error as e:
                print(e)

            finally:
                users2 = {}
                users2['set'] = 'send users'
                users2['users'] = users
                dec = json.dumps(users2)
                enc = dec.encode('utf-8')
                self.transport.write(enc)
                cursor.close()
                conn.close()
    def connectionLost(self, reason):
         print('dissconeted, reason:', reason)
         self.factory.numProtocols =- 1
class ChatFactory(Factory):
    def __init__(self):
        self.client = []
        self.ips = []
        self.numProtocols = 0
    def buildProtocol(self, addr):
        self.addr = addr
        return Chat(self,addr)
reactor.listenTCP(port,ChatFactory())
reactor.run()

