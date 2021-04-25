from twisted.internet import reactor, protocol, task, threads
from twisted.internet.protocol import ClientFactory, Protocol
import time
port = 9090
# Клиент  который  использует  абрику  для  создание   нового ПРОТОКОЛА  для  вычитывания даннх с  сервера

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

     def authLogin(self, data):
        print('auth login = ' + data.decode("utf-8"))
        time.sleep(3)
        self.transport.write('send data from 1-st'.encode("utf-8"))

     def dataReceived(self, data: str):
         print( data.decode("utf-8"))
         # Вся  эта  логика  для примера !!!!!!!!!!
         # Эта проверка для того что бы показать, что ожидание данных для консольного  клиента  блокирует весь клиент.
         # В сервере  есть  логика  где  заложено  что отдаль ответ, где пользователь  авторизован
         if data.decode("utf-8") == str('ok'):
            self.authLogin(data)
         else :
            self.sendMessage()

     def connectionMade(self):
         print('connected')
         self.sendMessage()

class ClientGetMessages(Protocol):

    def authLogin(self, data):
        print('get message = ' + data.decode("utf-8"))
        # Make transformation with  messages if they exists.
        time.sleep(5)
        self.transport.write('wait for data'.encode("utf-8"))

    def dataReceived(self, data: str):
        self.authLogin(data)

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

# Можно  сделать  какуе то  глобальную  переменную  для  того что бы передавая  на сервер  понимать  можно ли выдавать ил нет  сообщения  для  клиента


reactor.connectTCP('localhost',port, ClientChatFactory())
reactor.connectTCP('localhost',port, ClientChatFactory(ClientGetMessages()))
reactor.run()

