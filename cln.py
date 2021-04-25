import json
from twisted.internet import reactor, protocol, task
from twisted.internet.protocol import ClientFactory, Protocol
import time
port = 9090
check = input('Do you registred, already?')
name = []
registered = False
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
         if check == 'yes' and registered == False and strick['set'] == 'Hello from server':
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
         elif strick['set'] == 'GET':
             del strick['set']
             print(strick['mesg'])
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
         elif strick['set'] == 'auth':
             registered = True
             ClientGetMessages.dataReceived(self,data='GET')
         elif strick['set'] == 'bring':
             ClientGetMessages.dataReceived(self,data='GET')
         elif strick['set']== 'no mesg' and registered==True:
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
     def connectionLost(self, reason):
         print('disconnected, reason:', reason)
class ClientGetMessages(Protocol):
    def connectionMade(self):
        print('Get message connected')
    def dataReceived(self, data):
        if data =='GET':
            set = {}
            b = ''.join(name)
            set['nick'] = b
            set['set'] = 'Get'
            data2 = json.dumps(set)
            a = data2.encode('utf-8')
            self.transport.write(a)
    def connectionLost(self):
        print('disconected')
class ClientChatFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('connect..')
    def buildProtocol(self, addr):
         return ClientChat()
    def clientConnectionFailed(self, connector, reason):
        print('ConnectionFailed, reason:', reason)
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print('ConnectionLost, reason:', reason)
        connector.connect()
reactor.connectTCP('localhost',port, ClientChatFactory())
reactor.run()

