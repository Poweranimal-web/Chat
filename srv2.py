import builtins
import os
import json
from twisted.internet.protocol import Factory, Protocol
from write_data import insert_book
from check_data import query_with_fetchone1
from write_data2 import insert_book1
from Check_data2 import query_with_fetchone
from delete_data import delete_book
from find_friends import find_friend
from Check_data3 import query_with_fetchall
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from twisted.protocols.policies import TimeoutMixin
from twisted.internet import error
from twisted.python import log
from twisted.internet import reactor, protocol
port = 9090
information_file = {}
class Chat(Protocol, TimeoutMixin):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = addr
    def connectionMade(self):
       self.factory.numProtocols =+1
       print(self.factory.numProtocols)
       hi = {}
       hi['set'] = 'Hello from server'
       a = json.dumps(hi)
       self.transport.write(a.encode('utf-8'))
       log.startLogging(open(r'C:\Users\millioner\PycharmProjects\Chat\foo.log', 'w'))
    def dataReceived(self, data):
        global infromation_file
        try:
            d = data.decode('utf-8')
            struc = json.loads(d)
        except builtins.UnicodeDecodeError:
                Chat2.dataReceived(self, data=data)
        else:
            if struc['set'] == 'auth':
                        del struc['set']
                        login = struc['login']
                        password = struc['password']
                        a = query_with_fetchone1(login, password)
                        auth = {}
                        auth['set'] = 'auth'
                        c = json.dumps(auth)
                        no_auth = {}
                        no_auth['set'] = 'no auth'
                        g = json.dumps(no_auth)
                        if a == True:
                            self.transport.write(c.encode('utf-8'))
                        else:
                            self.transport.write(g.encode('utf-8'))
            elif struc['set'] == 'registr':
                        del struc['set']
                        login = struc['login']
                        password = struc['password']
                        insert_book(login, password)
                        auth = {}
                        auth['set'] = 'auth'
                        k = json.dumps(auth)
                        self.transport.write(k.encode('utf-8'))
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
                        q = query_with_fetchall(login)
                        delete_book(login)
                        if q['set'] == 'no':
                            no_mesg = {}
                            no_mesg['set'] = 'no mesg'
                            a = json.dumps(no_mesg)
                            self.transport.write(a.encode('utf-8'))
                        else:
                            cr = json.dumps(q)
                            self.transport.write(cr.encode('utf-8'))
            elif struc['set'] == 'find friend':
                        answer = {}
                        answer2 = {}
                        del struc['set']
                        c = struc['user']
                        b = find_friend(c)
                        answer['set'] = 'OK'
                        answer2['set'] = 'NO'
                        g = json.dumps(answer)
                        h = json.dumps(answer2)
                        if b == True:
                            self.transport.write(g.encode('utf-8'))
                        else:
                            self.transport.write(h.encode('utf-8'))
            elif struc['set'] == 'bring file':
                        os.mkdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % struc['receipient'])
                        del struc['set']
                        print('Received')
                        with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (struc['receipient'], struc['filename']), 'w') as f:
                            f.write(struc['datafile'])
            elif struc['set'] == 'bring file2':
                        del struc['set']
                        information_file['receipient'] = struc['receipient']
                        information_file['filename'] = struc['filename']
                        information_file['file_extension'] = struc['file_extension']
                        Chat2.dataReceived(self,data=b'OK')
            elif struc['set'] == 'Check File':
                        del struc['set']
                        if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % struc['dir']) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" %struc['dir']):
                             if len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s' % struc['dir'])) > 0:
                                a = len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s'% struc['dir'])) * 2
                                input_dir = r'C:\Users\millioner\PycharmProjects\Chat\Files\%s' % struc['dir']
                                c = {}
                                for root, dirs, filenames in os.walk(input_dir):
                                     for filename in filenames:
                                            c['filename'] = filename
                                            c['set'] = 'get'
                                            string = json.dumps(c)
                                            self.transport.write(string.encode('utf-8'))
                                            break
                             else:
                                 print('no file')
                                 no_file = {}
                                 no_file['set'] = 'no file'
                                 self.transport.write((json.dumps(no_file)).encode('utf-8'))
                        else:
                            print('no exist')
                            no_file = {}
                            no_file['set'] = 'no exist'
                            self.transport.write((json.dumps(no_file)).encode('utf-8'))
            elif struc['set'] == 'transport file':
                del struc['set']
                input_dir = r'C:\Users\millioner\PycharmProjects\Chat\Files\%s' % struc['dir']
                for root, dirs, filenames in os.walk(input_dir):
                    for filename in filenames:
                        with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (struc['dir'] , filename), 'rb') as f:
                            # enlargement = os.path.splitext(base)[1]
                            dataf = f.read()
                            self.transport.write(dataf)
                            f.close()
                            os.remove("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (struc['dir'], filename))
                            break

    def connectionLost(self, reason):
         print('dissconeted, reason:', reason)
         self.factory.numProtocols =- 1
class Chat2(Protocol):
    def dataReceived(self, data):
        if data == b'OK':
            r = {}
            r['set'] = 'get'
            v = json.dumps(r)
            m = v.encode('utf-8')
            self.transport.write(m)
        else:
            if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s" %(information_file['receipient'])) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % (information_file['receipient'])):
                with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (information_file['receipient'],information_file['filename']), 'wb') as f:
                    f.write(data)

            else:
                os.mkdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % (information_file['receipient']))
                with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (information_file['receipient'],information_file['filename']), 'wb') as f:
                    f.write(data)

class ChatFactory(Factory):
    def __init__(self):
        self.client = []
        self.ips = []
        self.numProtocols = 0
    def buildProtocol(self, addr):
        self.addr = addr
        return Chat(self,addr)
reactor.listenTCP(port, ChatFactory())
reactor.run()

