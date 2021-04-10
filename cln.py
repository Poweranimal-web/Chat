from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory, Protocol
port = 9090
class ClientChat(Protocol):
     def connectionMade(self):
         print('connected')
     def dataReceived(self, data: str):
          self.count = 0
          self.count =+ 1
          nick = input('Write your nickname ').encode('utf-8')
          self.transport.write(nick)
          if self.count == 1:
             self.count =+1
             self.transport.write('Choose which one you send message'.encode('utf-8'))
             print(data)
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
