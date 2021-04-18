import json
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, Protocol
port = 9090
class Chat(Protocol):
    def __init__(self, factory, addr):
        self.factory = (factory)
        self.factory.addr = str(addr)
    def connectionMade(self):
       self.factory.ips.append(self.factory.addr)
       self.factory.numProtocols =+1
       self.transport.write('Hello from server'.encode('utf-8'))
    def dataReceived(self, data):
        d = data.decode('utf-8')
        struc = json.loads(d)
        if struc['set'] == 'auth':
            del struc['set']
            f = open('user.txt', 'w+')
            str = json.dumps(struc)
            if str in f:
                self.transport.write('You are authorithed.Welcome %' % struc['login'].encode('utf-8'))
            else:
                self.transport.write('Wrong data, pls try again'.encode('utf-8'))
        elif struc['set'] == 'registr':
            global count
            del struc['set']
            struc['addres'] = self.factory.addr
            with open('user.txt', 'w') as f:
                json.dump(struc, f)
            self.transport.write(('Welcome , you are registred').encode('utf-8'))
        elif struc['set'] == 'write message':
            del struc['set']
            message = {}
            message1 = "{}:{}".format(struc['sender'], struc['message'])
            c = struc['receipient']
            message[c] = message1
            with open('message.txt', 'w') as f:
                json.dump(message + '\n', f)
        elif struc['set'] == 'Get':
            with open('message.txt', 'w+') as f:
                file = json.load(f)
                for key ,value in file:
                    self.transport.write((value).encode('utf-8'))
                    f = open('file.txt', 'w').close()
    def connectionLost(self, reason):
         print('dissconeted, reason:', reason)
         self.factory.numProtocols =- 1
         self.factory.ips.remove(self.factory.ips)
class ChatFactory(Factory):
    def __init__(self):
        self.client = []
        self.ips = []
        self.numProtocols = 0
    def buildProtocol(self, addr):
        self.addr = addr
        return Chat(self,addr)
reactor.listenTCP(port,ChatFactory())
reactor.run()

