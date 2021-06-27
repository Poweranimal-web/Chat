# Стабильно на python 2.7
# Скачать twisted и необходимый zope
# twistedmatrix.com/trac/wiki/Downloads
# pypi.python.org/pypi/zope.interface/4.1.2

# Twisted - управляемая событиями(event) структура
# Событиями управляют функции – event handler
# Цикл обработки событий отслеживает события и запускает соответствующие event handler
# Работа цикла лежит на объекте reactor из модуля twisted.internet

# Модуль socketserver для сетевого программирования
from twisted.internet import protocol, reactor


class Twist(protocol.Protocol):

    # Событие connectionMade срабатывает при соединении
    def connectionMade(self):
        self.file = open("/home/le__sage/tmp/image.jpg",'wb')
        print('connection success!')

    # Событие dataReceived - получение и отправление данных
    def dataReceived(self, data):
        print('length of  data={}'.format(len(data)))
        self.file.write(data)
        # transport.write - отправка сообщения
        self.transport.write('Hello from server!'.encode('utf-8'))

    # Событие connectionLost срабатывает при разрыве соединения с клиентом
    def connectionLost(self, reason):
        self.file.close()
        print('Connection lost!')


# Конфигурация поведения протокола описывается в – классе Factory из twisted.internet.protocol.Factory
factory = protocol.Factory()
factory.protocol = Twist
print('wait...')
reactor.listenTCP(7777, factory)
reactor.run()
