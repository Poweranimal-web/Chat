import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory, Protocol
port = 9090
class ClientChat(Protocol):
     def connectionMade(self):
         print('connected')
     def dataReceived(self, data: str):
         print(data)
         login = input('Enter your  login: ')
         password = input('Enter your password: ')
         data_auth = {}
         data_auth['login'] = login
         data_auth['password'] = password
         data2 = ','.join([f'{key},{value}' for key,value in data_auth.items()])
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
