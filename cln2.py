import json
from twisted.internet import reactor, protocol, task
from twisted.internet.protocol import ClientFactory, Protocol
import time
port = 9090
check = input('Do you registred, already?')
name = []
registered = False
showclients = False
tm = time.time()
class ClientChat(Protocol):
     def connectionMade(self):
         print('connected')
     def dataReceived(self, data):
         global check
         global name
         global registered
         c = data.decode('utf-8')
         strick = json.loads(c)
         if check == 'no' and registered == False and strick['set'] == 'Hello from server':
                login = input('Enter your  login: ')
                if login in name:
                    password = input('Enter your password: ')
                    data_auth = {}
                    data_auth['set'] = 'registr'
                    data_auth['login'] = login
                    data_auth['password'] = password
                    data2 = json.dumps(data_auth)
                    a = data2.encode('utf-8')
                    self.transport.write(a)
                else:
                    name.append(login)
                    password = input('Enter your password: ')
                    data_auth = {}
                    data_auth['set'] = 'registr'
                    data_auth['login'] = login
                    data_auth['password'] = password
                    data2 = json.dumps(data_auth)
                    a = data2.encode('utf-8')
                    self.transport.write(a)
         elif check == 'yes' and registered == False and strick['set'] == 'Hello from server':
                print('pls authoristing')
                login = input('Enter your login: ')
                if login in name:
                    password = input('Enter your password: ')
                    data_auth = {}
                    data_auth['login'] = login
                    data_auth['password'] = password
                    data_auth['set'] = 'auth'
                    data2 = json.dumps(data_auth)
                    a = data2.encode('utf-8')
                    self.transport.write(a)
                else:
                    name.append(login)
                    password = input('Enter your password: ')
                    data_auth = {}
                    data_auth['login'] = login
                    data_auth['password'] = password
                    data_auth['set'] = 'auth'
                    data2 = json.dumps(data_auth)
                    a = data2.encode('utf-8')
                    self.transport.write(a)
         elif strick['set'] =='no auth' and registered == False:
                name.pop()
                login = input('Enter your  login: ')
                if login in name:
                    password = input('Enter your password: ')
                    data_auth = {}
                    data_auth['set'] = 'auth'
                    data_auth['login'] = login
                    data_auth['password'] = password
                    data2 = json.dumps(data_auth)
                    a = data2.encode('utf-8')
                    self.transport.write(a)
                else:
                    name.append(login)
                    password = input('Enter your password: ')
                    data_auth = {}
                    data_auth['set'] = 'auth'
                    data_auth['login'] = login
                    data_auth['password'] = password
                    data2 = json.dumps(data_auth)
                    a = data2.encode('utf-8')
                    self.transport.write(a)
         elif strick['set'] == 'auth':
             registered = True
     def connectionLost(self, reason):
         print('disconnected, reason:', reason)
class ShowAllClients(Protocol):
    def connectionMade(self):
        print('cvvc')
    def dataReceived(self, data):
        global showclients
        c = data.decode('utf-8')
        strick2 = json.loads(c)
        set = {}
        set['set'] = 'GET USERS'
        data2 = json.dumps(set)
        a = data2.encode('utf-8')
        self.transport.write(a)
        if strick2['set'] == 'send users':
           showclients = True
           print(strick2['users'])
           print('Choose one')
    def connectionLost(self, reason):
        print('disconected')
class ClientGetMessages(Protocol):
    def connectionMade(self):
        print('Get message connected')
    def dataReceived(self, data):
            g = data.decode('utf-8')
            strick3 = json.loads(g)
            set = {}
            b = ''.join(name)
            set['nick'] = b
            set['set'] = 'Get'
            data2 = json.dumps(set)
            a = data2.encode('utf-8')
            self.transport.write(a)
            if strick3['set'] == 'no mesg':
                self.transport.write(a)
            elif strick3['set'] == 'GET':
                    print(strick3['mesg'])
    def connectionLost(self, reason):
        print('disconected')
class ClientWriteMessages(Protocol):
    def connectionMade(self):
        print('Get message connected')
    def dataReceived(self, data):
        data_login = {}
        choose = input('Choose one that send message:')
        message = input('Write message that you want send: ')
        b = ''.join(name)
        print(b)
        data_login['sender'] = b
        data_login['receipient'] = choose
        data_login['set'] = 'write message'
        data_login['message'] = message
        string = json.dumps(data_login)
        format_utf = string.encode('utf-8')
        self.transport.write(format_utf)
    def connectionLost(self, reason):
        print('disconected')
class ClientChatFactory(ClientFactory):
    def __init__(self, chat = ClientChat()):
        self.protocol = chat
    def startedConnecting(self, connector):
        print('connect..')
    def buildProtocol(self, addr):
         return self.protocol
    def clientConnectionFailed(self, connector, reason):
        print('ConnectionFailed, reason:', reason)
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print('ConnectionLost, reason:', reason)
        connector.connect()
def loopData():
    global tm
    global showclients
    print("registered={0}, time= {1}".format(registered, time.time()-tm))
    tm = time.time()
    if registered == False:
        reactor.connectTCP('localhost', port, ClientChatFactory())
    elif showclients == False:
        reactor.connectTCP('localhost', port, ClientChatFactory(ShowAllClients()))
    elif showclients == True:
        reactor.connectTCP('localhost', port, ClientChatFactory(ClientGetMessages()))
    elif registered == True and showclients == True:
        reactor.connectTCP('localhost', port, ClientChatFactory(ClientWriteMessages()))
loop = task.LoopingCall(loopData)
loop.start(2)
reactor.run()