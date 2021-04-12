import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
port = 9090
f = open('user.txt', 'w+')
class Chat(Protocol):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = str(addr)
    def connectionMade(self):
       self.factory.numProtocols =+1
       self.transport.write("Welcome! There are currently %d open connections" .encode('utf-8')%(self.factory.numProtocols))
    def dataReceived(self, data:str):
        self.factory.ips.append(self.factory.addr)
        print(type(self.factory.addr))
        # str1 = json.dumps(self.factory.addr)
        d = data.decode('utf-8')
        struc = json.loads(d)
        struc['addres'] = self.factory.addr
        str = json.dumps(struc)
        f.write(str)
        f.close()
        print('From Client:', struc)
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

