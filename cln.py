import json
from twisted.internet import reactor, protocol, task
from twisted.internet.protocol import ClientFactory, Protocol
port = 9090
check = input('Do you registred, already?')
timeout = 10.0
class ClientChat(Protocol):
     def connectionMade(self):
         print('connected')
     def dataGet(self, data):
         decode = data.decode('utf-8')
         print(decode)
         set = {}
         set['set'] = 'Get'
         data2 = json.dumps(set)
         a = data2.encode('utf-8')
         self.transport.write(a)
     l = task.LoopingCall(dataGet)
     l.start(timeout)
     def dataReceived(self, data):
         global check
         c = data.decode('utf-8')
         print(c)
         if c == 'Welcome , you are registred':
             data_login = {}
             choose = input('Choose one that send message:')
             message = input('Write message that you want send: ')
             name = input('Enter your name: ')
             data_login['sender'] = name
             data_login['receipient'] = choose
             data_login['set'] = 'write message'
             data_login['message'] = message
             string = json.dumps(data_login)
             format_utf = string.encode('utf-8')
             self.transport.write(format_utf)
         elif check == 'no':
             login = input('Enter your  login: ')
             password = input('Enter your password: ')
             data_auth = {}
             data_auth['set'] = 'registr'
             data_auth['login'] = login
             data_auth['password'] = password
             data2 = json.dumps(data_auth)
             a = data2.encode('utf-8')
             self.transport.write(a)
         elif check == 'yes':
            c = data.decode('utf-8')
            print(c)
            print('pls authoristing')
            login = input('Enter your login: ')
            password = input('Enter your password: ')
            data_auth = {}
            data_auth['login'] = login
            data_auth['password'] = password
            data_auth['set'] = 'auth'
            data2 = json.dumps(data_auth)
            a = data2.encode('utf-8')
            self.transport.write(a)
     def connectionLost(self, reason):
         print('disconnected, reason:', reason)
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
