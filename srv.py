import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
from twisted.protocols.basic import LineReceiver
port = 9090
f = open('user.txt', 'w+')
class Chat(Protocol):
    def __init__(self, factory, addr):
        self.factory = factory
        self.factory.addr = str(addr)
    def connectionMade(self):
       self.factory.numProtocols =+1
       self.transport.write('Hello from server'.encode('utf-8'))
    def dataReceived(self, data):
        d = data.decode('utf-8')
        struc = json.loads(d)
        if struc['set'] == 'auth':
            del struc['set']
            str = json.dumps(struc)
            if str in f:
                self.transport.write('You are authorithed.Welcome %' % struc['login'].encode('utf-8'))
            else:
                self.transport.write('Wrong data, pls try again'.encode('utf-8'))
        elif struc['set'] == 'registr':
            del struc['set']
            struc['addres'] = self.factory.addr
            str = json.dumps(struc)
            f.write(str)
            f.close()
            self.transport.write(('Welcome %s , you are registred' % struc['login']).encode('utf-8'))
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

