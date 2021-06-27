import os
from twisted.internet import protocol, reactor

host = '127.0.0.1'
port = 7777


class Twist_client(protocol.Protocol):

    def __init__(self, name = 'test_pic.jpg'):
        # Здесь пропишешь свои пути откуда  брать файл и куда  перемещать его после отправки или  уадаляй после  отправки
        self.path_from = '/home/le__sage/tmp/'
        self.path_move = '/home/le__sage/tmp/send/'
        self.file = name

    def sendData(self):
        if os.path.isfile( self.path_from+self.file):
            image = open(self.path_from+self.file,'rb')
            data = image.read()
            if data:
                print('length of  data ={}'.format(len(data)))
                self.transport.write(data)
                os.rename( self.path_from+self.file, self.path_move+self.file)
            else:
                # transport.loseConnection() - разрыв соединения
                self.transport.loseConnection()
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()


class Twist_Factory(protocol.ClientFactory):

    def __init__(self, name ):
        self.name = name
        self.protocol = Twist_client(name)

    def buildProtocol(self, addr):
        return self.protocol

    def clientConnectionFailed(self, connector, reason):
        print('connection failed:', reason.getErrorMessage())
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print ('connection lost:', reason.getErrorMessage())
        reactor.stop()

# Передаешь имя файла который  у  тебя  лежит в указаных путях
factory = Twist_Factory( 'test_pic2.jpg')
reactor.connectTCP(host, port, factory)
reactor.run()