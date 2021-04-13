import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory, Protocol
from twisted.protocols.basic import LineReceiver
port = 9090
check = input('Do you registred, already?')
class ClientChat(Protocol):
     def connectionMade(self):
         print('connected')
     def dataReceived(self, data):
         global check
         print(data)
         if check == 'no':
             check1 = check.encode('utf-8')
             self.transport.write(check1)
         elif check == 'yes':
             check1 = check.encode('utf-8')
             self.transport.write(check1)
class ClientChat2(ClientChat):
     def dataReceived(self, data):
         if check == 'no':
             print(data)
             login = input('Enter your  login: ')
             password = input('Enter your password: ')
             data_auth = {}
             data_auth['login'] = login
             data_auth['password'] = password
             data2 = json.dumps(data_auth)
             a = data2.encode('utf-8')
             self.transport.write(a)
         elif check == 'yes':
            print(data)
            print('pls authoristing')
            login = input('Enter your login: ')
            password = input('Enter your password: ')
            data_auth = {}
            data_auth['login'] = login
            data_auth['password'] = password
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
