import builtins
import os
import json
from twisted.internet.protocol import Factory, Protocol
from write_data import insert_user
from check_data import query_with_fetchone1
from write_data2 import insert_message
from Check_data2 import query_with_fetchone
from delete_data import delete_message
from find_friends import find_friend
from Check_data3 import query_with_fetchall
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from twisted.protocols.policies import TimeoutMixin
from  twisted.internet.interfaces import IConsumer
from twisted.internet import error
from twisted.python import log
from twisted.internet import reactor, protocol
from twisted.protocols.basic import FileSender
port = 9090
information_file = {}
class Chat(Protocol, TimeoutMixin):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = addr
    def connectionMade(self):
       self.factory.numProtocols =+1
       print(self.factory.numProtocols)
       hi_from_server = {}
       hi_from_server['set'] = 'Hello from server'
       self.transport.write(json.dumps(hi_from_server).encode('utf-8'))
       # log.startLogging(open(r'C:\Users\millioner\PycharmProjects\Chat\foo.log', 'w'))
    def dataReceived(self, data):
        global infromation_file
        try:
            get_data = data.decode('utf-8')
            get_data_in_dict = json.loads(get_data)
        except builtins.UnicodeDecodeError:
                Chat2.dataReceived(self, data=data)
        else:
            if get_data_in_dict['set'] == 'auth':
                            del get_data_in_dict['set']
                            login = get_data_in_dict['login']
                            password = get_data_in_dict['password']
                            answer_db = query_with_fetchone1(login, password)
                            auth = {}
                            auth['set'] = 'auth'
                            no_auth = {}
                            no_auth['set'] = 'no auth'
                            if answer_db == True:
                                self.transport.write(json.dumps(auth).encode('utf-8'))
                            else:
                                self.transport.write(json.dumps(no_auth).encode('utf-8'))
            elif get_data_in_dict['set'] == 'registr':
                            del get_data_in_dict['set']
                            login = get_data_in_dict['login']
                            password = get_data_in_dict['password']
                            insert_user(login, password)
                            auth = {}
                            auth['set'] = 'auth'
                            self.transport.write(json.dumps(auth).encode('utf-8'))
            elif get_data_in_dict['set'] == 'write message':
                            del get_data_in_dict['set']
                            message = "{}:{}".format(get_data_in_dict['sender'], get_data_in_dict['message'])
                            c = get_data_in_dict['receipient']
                            insert_message(c, message)
                            bring = {}
                            bring['set'] = 'bring'
                            self.transport.write(json.dumps(bring).encode('utf-8'))
            elif get_data_in_dict['set'] == 'Get':
                            del get_data_in_dict['set']
                            login = get_data_in_dict['nick']
                            request_message = query_with_fetchall(login)
                            delete_message(login)
                            if request_message['set'] == 'no':
                                no_mesg = {}
                                no_mesg['set'] = 'no mesg'
                                self.transport.write(json.dumps(no_mesg).encode('utf-8'))
                            else:
                                self.transport.write(json.dumps(request_message).encode('utf-8'))
            elif get_data_in_dict['set'] == 'find friend':
                            answer = {}
                            answer2 = {}
                            del get_data_in_dict['set']
                            answer3 = find_friend(get_data_in_dict['user'])
                            answer['set'] = 'OK'
                            answer2['set'] = 'NO'
                            if answer3 == True:
                                self.transport.write(json.dumps(answer).encode('utf-8'))
                            else:
                                self.transport.write(json.dumps(answer2).encode('utf-8'))
            elif get_data_in_dict['set'] == 'bring file':
                        os.mkdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % get_data_in_dict['receipient'])
                        del get_data_in_dict['set']
                        print('Received')
                        with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (get_data_in_dict['receipient'], get_data_in_dict['filename']), 'w') as f:
                            f.write(get_data_in_dict['datafile'])
            elif get_data_in_dict['set'] == 'bring file2':
                        del get_data_in_dict['set']
                        information_file['receipient'] = get_data_in_dict['receipient']
                        information_file['filename'] = get_data_in_dict['filename']
                        information_file['file_extension'] = get_data_in_dict['file_extension']
                        Chat2.dataReceived(self,data=b'OK')
            elif get_data_in_dict['set'] == 'Check File':
                        del get_data_in_dict['set']
                        if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % get_data_in_dict['dir']) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" %get_data_in_dict['dir']):
                             if len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s' % get_data_in_dict['dir'])) > 0:
                                a = len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s'% get_data_in_dict['dir'])) * 2
                                input_dir = r'C:\Users\millioner\PycharmProjects\Chat\Files\%s' % get_data_in_dict['dir']
                                c = {}
                                for root, dirs, filenames in os.walk(input_dir):
                                     for filename in filenames:
                                            c['filename'] = filename
                                            c['set'] = 'get'
                                            self.transport.write(json.dumps(c).encode('utf-8'))
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
            elif get_data_in_dict['set'] == 'transport file':
                del get_data_in_dict['set']
                input_dir = r'C:\Users\millioner\PycharmProjects\Chat\Files\%s' % get_data_in_dict['dir']
                for root, dirs, filenames in os.walk(input_dir):
                    for filename in filenames:
                        with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (get_data_in_dict['dir'] , filename), 'rb') as f:
                            # enlargement = os.path.splitext(base)[1]
                            dataf = f.read()
                            self.transport.write(dataf)
                            f.close()
                            os.remove("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (get_data_in_dict['dir'], filename))
                            break

    def connectionLost(self, reason):
         print('dissconeted, reason:', reason)
         self.factory.numProtocols =- 1
class Chat2(Protocol):
    def dataReceived(self, data):
        print(data)
        if data == b'OK':
            r = {}
            r['set'] = 'get'
            self.transport.write(json.dumps(r).encode('utf-8'))
        else:
            if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % (information_file['receipient'])) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % (information_file['receipient'])):
                f = open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % (information_file['receipient'], information_file['filename']), 'wb')
                f.write(data)
                f.close()
            else:
                os.mkdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s" % (information_file['receipient']))
                f = open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/%s" % ( information_file['receipient'], information_file['filename']), 'wb')
                f.write(data)
                f.close()
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

