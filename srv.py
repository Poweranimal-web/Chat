import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
port = 9090
class Chat(Protocol):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = addr
    def connectionMade(self):
       self.factory.numProtocols =+1
       self.transport.write("Welcome! There are currently %d open connections" .encode('utf-8')%(self.factory.numProtocols))
    def dataReceived(self, data):
        self.factory.ips.append(self.factory.addr)
        b = data
        a = json.dumps(b)
        print('From Client:', a)
        self.transport.write('Server  Answer.The data was received from client '.encode('utf-8'))
        # a = str(data)
        # b = self.factory.addr
        # self.factory.users[a] = b
        # if self.factory.numProtocols == 2:
        #     self.factory.ips.transport.write(self.factory.users[a])
    def connectionLost(self, reason):
         print('dissconeted, reason:', reason)
         self.factory.numProtocols =- 1
         self.factory.ips.remove(self.factory.addr)
class ChatFactory(Factory):
    def __init__(self):
        self.ips = []
        self.nick = []
        self.users = {}
        self.numProtocols = 0
    def buildProtocol(self, addr):
        self.addr = addr
        return Chat(self,addr)
reactor.listenTCP(port,ChatFactory())
reactor.run()

