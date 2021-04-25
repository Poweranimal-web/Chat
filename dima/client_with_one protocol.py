from twisted.internet import reactor, protocol, task, threads
from twisted.internet.protocol import ClientFactory, Protocol
import time
port = 9090
class ClientChat(Protocol):

     def __init__(self):
         self.authorized = False
         self.message = []


     def sendRegistry(self):
         # Отправка  запроса  с  параметрами регистрации
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

     def sendAuth(self):
        # Отправка для аворизации
        pass

     def sendMessage(self):
        # Отправка  сообщения  другому  клиенту , через  сервер
        pass

     def getMessages(self, data):
        # Тут  написать  логику для  обработки  входящего пакета  от сервера
        time.sleep(3)
        self.transport.write('request for  get messages'.encode("utf-8"))


     def dataReceived(self, data: str):
         # Тут  отслеживать что прислал сервер  и  запускать нужный метод
         # То есть  посторить  логику  последовательной  обработки, если пришел ответ с сообщениями, то выполнить этот метод.
         # Но в  таком  подходе  надо что  бы  и серер  высылал  определенные  параметры  о том  какой  ответ он отправил.
         print( data.decode("utf-8"))
         if data.decode("utf-8") == str('ok'):
             self.authorized = True

         if self.authorized:
            self.authLogin(data)
         else :
            self.sendMessage()

     def connectionMade(self):
         print('connected')
         self.sendMessage()


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


reactor.connectTCP('localhost',port, ClientChatFactory())
reactor.run()

