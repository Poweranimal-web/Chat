import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
from write_data import insert_book
from check_data import query_with_fetchone1
from write_data2 import insert_book1
from Check_data2 import query_with_fetchone
from delete_data import delete_book
port = 9090
class Chat(Protocol):
    def __init__(self, factory, addr):
        self.factory = (factory)
        self.factory.addr = addr
    def connectionMade(self):
       self.factory.ips.append(self.factory.addr)
       self.factory.numProtocols =+1
       self.transport.write('Hello from server'.encode('utf-8'))
    def dataReceived(self, data):
        d = data.decode('utf-8')
        struc = json.loads(d)
        if struc['set'] == 'auth':
            del struc['set']
            login = struc['login']
            password = struc['password']
            a = query_with_fetchone1(login, password)
            if a == True:
                self.transport.write('Welcome , you are registred'.encode('utf-8'))
            else:
                self.transport.write('Wrong data, try again('.encode('utf-8'))
        elif struc['set'] == 'registr':
            del struc['set']
            login = struc['login']
            password = struc['password']
            insert_book(login, password)
            self.transport.write(('Welcome , you are registred').encode('utf-8'))
        elif struc['set'] == 'write message':
            del struc['set']
            message = "{}:{}".format(struc['sender'], struc['message'])
            c = struc['receipient']
            insert_book1(c, message)
            self.transport.write('message sent'.encode('utf-8'))
        elif struc['set'] == 'Get':
            del struc['set']
            login = struc['nick']
            list = []
            b = query_with_fetchone(login)
            string = str(b)
            list.append(string)
            list.append('GET')
            delete_book(login)
            if b == False:
                self.transport.write('No messages(('.encode('utf-8'))
            else:
                self.transport.write((string).encode('utf-8'))
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

