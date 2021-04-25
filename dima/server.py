from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
from sys import stdout
port = 9090
count = 0
class Chat(Protocol):

    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = addr
        self.count = 0

    def connectionMade(self):
       self.factory.ips.append(self.factory.addr)
       self.dataReceived
       print ( 'factory array ',  self.factory.nick)
       g = self.factory.nick
       c = ''
       r = c.join(g)
       b = self.factory.addr
       self.factory.users[r] = b

    def connectionLost(self, reason):
         self.factory.ips.remove(self)

    def dataReceived(self, data:str):
        print('count {0}'.format(self.count))
        self.count = self.count + 1
        # Это симуляция того что  прошла авторизация
        if self.count>2:
            a = data.decode('utf-8')
            print('From Client:', data)
            self.transport.write('ok'.encode('utf-8'))
        else :
            a = data.decode('utf-8')
            print('From Client:', data)
            self.transport.write('Server  Answer.The data was received from client '.encode('utf-8'))

class ChatFactory(Factory):

    def __init__(self):
        self.ips = []
        self.nick = []
        self.users = {}

    def buildProtocol(self, addr):
        self.addr = addr
        return Chat(self,addr)


reactor.listenTCP(port,ChatFactory())
reactor.run()

