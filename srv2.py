import builtins
import time
import os
import shutil
import json
import ndjson
import uuid
import gzip
from pathlib import Path
from twisted.internet.protocol import Factory, Protocol
from write_data import insert_user
from check_data import query_with_fetchone1
from write_data2 import insert_message
from write_data3 import insert_message4
from write_data4 import insert_message5
from Check_data2 import query_with_fetchone
from delete_data import delete_message
from find_friends import find_friend
from Check_data3 import query_with_fetchall
from return_message import get_message
from change_data2 import change_status
from change_data3 import change_status3
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from twisted.protocols.policies import TimeoutMixin
import psutil
from twisted.internet.interfaces import IConsumer
from twisted.internet import error
from twisted.python import log
from twisted.internet import reactor, protocol
from twisted.protocols.basic import FileSender
port = 6002
information_file = {}
information_fil = {}
file_name = {}
File = True
class Chat(Protocol, TimeoutMixin):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = addr
    def connectionMade(self):
        self.factory.numProtocols = +1
        print(self.factory.numProtocols)
        hi_from_server = {}
        hi_from_server['set'] = 'Hello from server'
        self.transport.write(json.dumps(hi_from_server).encode('utf-8'))
    def dataReceived(self, data):
        global infromation_file
        try:
            get_data = data.decode('utf-8')
            get_data_in_dict = json.loads(get_data)
            print(get_data_in_dict)
        except builtins.UnicodeDecodeError:
            try:
              Chat2.dataReceived(self, data=data)
            except builtins.AttributeError:
                decompress_data = gzip.decompress(data)
                decode_data = decompress_data.decode('utf-8')
                get_data_in_dict = json.loads(decode_data)
                if get_data_in_dict['set'] == 'transport txt file':
                    del get_data_in_dict['set']
                    with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (information_file['receipient'],information_file['filename'] ), 'w') as f:
                        f.write(get_data_in_dict['datafile'])
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
                message = "{}".format(get_data_in_dict['message'])
                message2 = "{}:{}".format(get_data_in_dict['sender'], get_data_in_dict['message'])
                c = get_data_in_dict['receipient']
                insert_message(c, message2)
                insert_message5(get_data_in_dict['sender'], c, message, status=False)
                insert_message4(c, get_data_in_dict['sender'], message2, status=True)
                bring = {}
                bring['set'] = 'bring'
                self.transport.write(json.dumps(bring).encode('utf-8'))
            elif get_data_in_dict['set'] == 'Get':
                del get_data_in_dict['set']
                login = get_data_in_dict['nick']
                request_message = query_with_fetchall(login)
                delete_message(login)
                if request_message == False:
                    no_mesg = {}
                    no_mesg['set'] = 'no mesg'
                    self.transport.write(json.dumps(no_mesg).encode('utf-8'))
                else:
                    self.transport.write(json.dumps(request_message, ensure_ascii=False).encode('utf-8'))
            elif get_data_in_dict['set'] == 'GET':
                # log.startLogging(open('/home/cstores/Chat/foo.log', 'w'))
                del get_data_in_dict['set']
                login = get_data_in_dict['login']
                sender = get_data_in_dict['sender']
                change_status3(status=True, login=login, sender=sender)
                result = get_message(login, sender)
                status = False
                if result == False:
                    no_mesg = {}
                    no_mesg['set'] = 'no mess'
                    self.transport.write(json.dumps(no_mesg).encode('utf-8'))
                    self.transport.loseConnection()
                else:
                    change_status_message = change_status(status, sender)
                    self.transport.write(gzip.compress((json.dumps(result, ensure_ascii=False)).encode('utf-8')))
                    self.transport.loseConnection()
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
                del get_data_in_dict['set']
                information_file['receipient'] = get_data_in_dict['receipient']
                information_file['file_extension'] = get_data_in_dict['file_extension']
                information_file['file_size'] = get_data_in_dict['filesize']
                if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % (information_file['receipient'])) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % (information_file['receipient'])):
                    filename = str(uuid.uuid4().hex + information_file['file_extension'])
                    information_file['filename'] = filename
                    response = {}
                    response['set'] = 'trans txt'
                    self.transport.write(json.dumps(response).encode('utf-8'))
                else:
                    Path("/home/cstores/Chat/Files/%s" % get_data_in_dict['receipient']).mkdir(parents=True,
                                                                                               exist_ok=True)
                    Path("/home/cstores/Chat/Files/%s/backup copy" % get_data_in_dict['receipient']).mkdir(parents=True,
                                                                                                           exist_ok=True)
                    Path("/home/cstores/Chat/Files/%s/transport file" % get_data_in_dict['receipient']).mkdir(
                        parents=True, exist_ok=True)
                    filename = str(uuid.uuid4().hex + information_file['file_extension'])
                    with open("/home/cstores/Chat/Files/%s/transport file/%s" % (get_data_in_dict['receipient'], filename), 'w') as f:
                        f.write(get_data_in_dict['datafile'])
            elif get_data_in_dict['set'] == 'bring file2':
                del get_data_in_dict['set']
                information_file['receipient'] = get_data_in_dict['receipient']
                information_file['file_extension'] = get_data_in_dict['file_extension']
                information_file['file_size'] = get_data_in_dict['filesize']
                information_fil['file_size'] = get_data_in_dict['filesize']
                if os.path.exists("/home/cstores/Chat/Files/%s/transport file" % (
                information_file['receipient'])) and os.path.isdir(
                        "/home/cstores/Chat/Files/%s/transport file" % (information_file['receipient'])):
                    filename = str(uuid.uuid4().hex + information_file['file_extension'])
                    information_file['file'] = filename
                    self.f = open(
                        "/home/cstores/Chat/Files/%s/transport file/%s" % (information_file['receipient'], filename),
                        'wb')
                    Chat2.dataReceived(self, data=b'OK')
                else:
                    Path("/home/cstores/Chat/Files/%s" % get_data_in_dict['receipient']).mkdir(parents=True,
                                                                                               exist_ok=True)
                    Path("/home/cstores/Chat/Files/%s/backup copy" % get_data_in_dict['receipient']).mkdir(parents=True,
                                                                                                           exist_ok=True)
                    Path("/home/cstores/Chat/Files/%s/transport file" % get_data_in_dict['receipient']).mkdir(
                        parents=True, exist_ok=True)
                    filename = str(uuid.uuid4().hex + information_file['file_extension'])
                    self.f = open("/home/cstores/Chat/Files/%s/transport file/%s" % (
                        information_file['receipient'], filename), 'wb')
                    Chat2.dataReceived(self, data=b'OK')
            elif get_data_in_dict['set'] == 'Check File':
                information_file['dirs'] = get_data_in_dict['dirs']
                del get_data_in_dict['set']
                if os.path.exists("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % get_data_in_dict['dirs']) and os.path.isdir("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file" % get_data_in_dict['dirs']):
                    if len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file' % get_data_in_dict['dirs'])) > 0:
                        a = len(os.listdir('C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file' % get_data_in_dict['dirs'])) * 2
                        input_dir = 'C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file' % get_data_in_dict['dirs']
                        c = {}
                        for root, dirs, filenames in os.walk(input_dir):
                            for filename in filenames:
                                c['filename'] = filename
                                information_file['filename'] = filename
                                c['size'] = os.stat('C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s' % (
                                get_data_in_dict['dirs'], filename)).st_size
                                print('size={}'.format(c['size']))
                                file_ex = os.path.splitext(filename)[1]
                                file_exp = ''.join(file_ex)
                                c['set'] = 'get'
                                if file_exp == '.jpg' or file_exp == '.jpeg' or file_exp == '.png' or file_exp == '.pdf':
                                    self.transport.write(json.dumps(c).encode('utf-8'))
                                    break
                                else:
                                    c['set'] = 'get another file'
                                    c['filename'] = filename
                                    c['size'] = os.stat('C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s' % (get_data_in_dict['dirs'], filename)).st_size
                                    with open("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (get_data_in_dict['dirs'], filename), 'r') as f:
                                        data_read = f.read()
                                        c['filedata'] = data_read
                                        statinfo = os.stat("C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (get_data_in_dict['dirs'], filename))
                                        size = int(statinfo.st_size)
                                        if size >= 10000:
                                            data_in_json = json.dumps(c)
                                            data_in_encode = data_in_json.encode('utf-8')
                                            compress_data = gzip.compress(data_in_encode)
                                            self.transport.write(compress_data)
                                            break
                                        else:
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
            elif get_data_in_dict['set'] == 'Nice':
                del get_data_in_dict['set']
                source_dir = "C:/Users/millioner/PycharmProjects/Chat/Files/%s/transport file/%s" % (
                information_file['dirs'], information_file['filename'])
                target_dir = "C:/Users/millioner/PycharmProjects/Chat/Files/%s/backup copy/%s" % (
                information_file['dirs'], information_file['filename'])
                os.replace(source_dir, target_dir)
            elif get_data_in_dict['set'] == 'transport file':
                del get_data_in_dict['set']
                input_dir = '/home/cstores/Chat/Files/%s/transport file' % information_file['dirs']
                for root, dirs, filenames in os.walk(input_dir):
                    for filename in filenames:
                        self.f2 = open(
                            "/home/cstores/Chat/Files/%s/transport file/%s" % (information_file['dirs'], filename),
                            'rb')
                        file_name['name'] = filename
                        dataf = self.f2.read()
                        print((len(dataf)))
                        self.transport.write(dataf)
                        self.f2.close()
                        source_dir = "/home/cstores/Chat/Files/%s/transport file/%s" % (
                        information_file['dirs'], file_name['name'])
                        target_dir = "/home/cstores/Chat/Files/%s/backup copy/%s" % (
                        information_file['dirs'], file_name['name'])
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
        return Chat(self, addr)
reactor.listenTCP(port, ChatFactory())
reactor.run()