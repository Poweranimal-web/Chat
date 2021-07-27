import builtins
import os
import shutil
import json
import uuid
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
import psutil
from  twisted.internet.interfaces import IConsumer
from twisted.internet import error
from twisted.python import log
from twisted.internet import reactor, protocol
from twisted.protocols.basic import FileSender
port = 9090
information_file = {}
information_fil ={}
file_name = {}
File = True
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
            print(get_data_in_dict)
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
                information_file['file_extension'] = get_data_in_dict['file_extension']
                information_file['file_size'] = get_data_in_dict['filesize']
                information_fil['file_size'] = get_data_in_dict['filesize']
                if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % (information_file['receipient'])) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % (information_file['receipient'])):
                    filename = str(uuid.uuid4().hex + information_file['file_extension'])
                    information_file['file'] = filename
                    self.f = open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (information_file['receipient'], filename), 'wb')
                    Chat2.dataReceived(self, data=b'OK')
                else:
                    os.mkdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s/backup copy" % get_data_in_dict['receipient'])
                    os.mkdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % get_data_in_dict['receipient'])
                    filename = str(uuid.uuid4().hex + information_file['file_extension'])
                    self.f = open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (
                     information_file['receipient'], filename), 'wb')
                    Chat2.dataReceived(self, data=b'OK')
            elif get_data_in_dict['set'] == 'Check File':
                information_file['dirs'] = get_data_in_dict['dirs']
                del get_data_in_dict['set']
                if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % get_data_in_dict['dirs']) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" %get_data_in_dict['dirs']):
                    if len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file' % get_data_in_dict['dirs'])) > 0:
                        a = len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file'% get_data_in_dict['dirs'])) * 2
                        input_dir = r'C:\Users\millioner\PycharmProjects\Chat\Files\%s\transport file' % get_data_in_dict['dirs']
                        c = {}
                        for root, dirs, filenames in os.walk(input_dir):
                            for filename in filenames:
                                c['filename'] = filename
                                c['size'] = os.stat(r'C:\Users\millioner\PycharmProjects\Chat\Files\%s\transport file\%s' %(get_data_in_dict['dirs'],filename)).st_size
                                print('size={}'.format(c['size']))
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
                input_dir = r'C:\Users\millioner\PycharmProjects\Chat\Files\%s\transport file' % information_file['dirs']
                for root, dirs, filenames in os.walk(input_dir):
                    for filename in filenames:
                        self.f2 = open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (information_file['dirs'] , filename), 'rb')
                        file_name['name'] = filename
                        dataf = self.f2.read()
                        print((len(dataf)))
                        self.transport.write(dataf)
                        self.f2.close()
                        source_dir = "C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (information_file['dirs'], file_name['name'])
                        target_dir = "C:/Users/millioner/PycharmProjects/Chat/Files/%s/backup copy/%s" % (information_file['dirs'], file_name['name'])
                        os.replace(source_dir, target_dir)
                        break
    def connectionLost(self, reason):
            try:
                self.f.close()
                print('dissconeted, reason:', reason)
                self.factory.numProtocols = - 1
            except builtins.AttributeError:
                        pass
class Chat2(Protocol):
    def dataReceived(self, data):
        global information_fil
        global information_file
        if data == b'OK':
            r = {}
            r['set'] = 'get'
            self.transport.write(json.dumps(r).encode('utf-8'))
        else:
            self.f.write(data)
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

