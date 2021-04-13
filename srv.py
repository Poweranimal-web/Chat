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
       self.dataReceived
    def dataReceveid1(self, data):
        d = data.decode('utf-8')
        struc = json.loads(d)
        struc['addres'] = self.factory.addr
        str = json.dumps(struc)
        if str in f:
            self.transport.write('You are authorithed.Welcome %' % struc['login'].encode('utf-8'))
        else:
            self.transport.write('Wrong data, pls try again'.encode('utf-8'))
    def dataReceveid2(self, data):
        d = data.decode('utf-8')
        struc = json.loads(d)
        struc['addres'] = self.factory.addr
        str = json.dumps(struc)
        f.write(str)
        f.close()
        self.transport.write('Welcome % , you are registred' % struc['login'].encode('utf-8'))
    def dataReceived(self, data):
        self.factory.ips.append(self.factory.addr)
        b = data.decode('utf-8')
        self.transport.write('data get'.encode('utf-8'))
        if b == 'yes':
             self.dataReceveid1(data=bytes)
        elif b == 'no':
             self.dataReceveid2(data=bytes)

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

