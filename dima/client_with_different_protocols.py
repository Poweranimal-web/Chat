from twisted.internet import reactor, protocol, task, threads
from twisted.internet.protocol import ClientFactory, Protocol
from twisted.web.client import Agent
from twisted.web.error import Error
import time
import random

port = 9090
# Клиент  который  использует  абрику  для  создание   нового ПРОТОКОЛА  для  вычитывания даннх с  сервера
answer=None
tm = time.time()
class ClientChat(Protocol):
     def sendMessage(self):
         login = input('Enter your  login')
         fio = input('Enter your  FIO:')
         addres = input('Enter  your  address:')
         a1 = {}
         a1['login'] = login
         a1['fio'] = fio
         a1['addres'] = addres
         data2 = ','.join([f'{key},{value}' for key, value in a1.items()])
         a = data2.encode('utf-8')
         self.transport.write(a)

     def dataReceived(self, data: str):
         global answer
         print( data.decode("utf-8"))
         answer=data.decode("utf-8")


     def connectionMade(self):
         print('connected')
         self.sendMessage()

class ClientGetMessages(Protocol):

    def authLogin(self, data):
        # time.sleep(5)
        self.transport.write('wait for data'.encode("utf-8"))

    def dataReceived(self, data: str):
        global answer
        answer = data.decode("utf-8")
        print('get message = ' + data.decode("utf-8"))


    def connectionMade(self):
        print('Get message connected')
        self.authLogin( 'Get message started'.encode("utf-8"))

class ClientChatFactory(ClientFactory):
    def __init__(self, chat = ClientChat()):
        self.protocol = chat
    def startedConnecting(self, connector):
        print('client chatFactory connected.')
    def buildProtocol(self, addr):
         return self.protocol
    def clientConnectionFailed(self, connector, reason):
        print('ConnectionFailed, reason:', reason)
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print('ConnectionLost, reason:', reason)
        connector.connect()


def loopData():
    global tm
    print("answer={0}, time= {1}".format(answer, time.time()-tm))
    tm = time.time()
    if answer == str('ok'):
        reactor.connectTCP('localhost', port, ClientChatFactory(ClientGetMessages()))
    else:
        reactor.connectTCP('localhost', port, ClientChatFactory())

loop = task.LoopingCall(loopData)
loop.start(2)
reactor.run()

