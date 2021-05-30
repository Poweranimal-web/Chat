import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
class InputBox(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(InputBox, self).__init__(parent)
        open_message = QtWidgets.QLabel("Enter Login:")
        self.txt = QtWidgets.QLineEdit()
        save = QtWidgets.QPushButton('add',   clicked=self.accept)
        cancel = QtWidgets.QPushButton('Cancel', clicked=self.reject)

        grid = QtWidgets.QGridLayout(self)
        grid.setSpacing(10)
        grid.addWidget(open_message, 0, 0)
        grid.addWidget(self.txt, 1, 0, 1, 2)
        grid.addWidget(save, 2, 0)
        grid.addWidget(cancel, 2, 1)
        self.setFixedSize(self.sizeHint())

    def save(self):
        value = self.txt.text()
        return value
class Ui_MainWindow2(object):
   def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(879, 550)
            MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.widget = QtWidgets.QWidget(self.centralwidget)
            self.widget.setGeometry(QtCore.QRect(240, 0, 641, 80))
            self.widget.setObjectName("widget")
            self.pushButton_5 = QtWidgets.QPushButton(self.widget)
            self.pushButton_5.setGeometry(QtCore.QRect(470, 10, 75, 51))
            self.pushButton_5.setStyleSheet("QPushButton{\n"
    "border:0px;\n"
    "\n"
    "\n"
    "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("phone-call.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_5.setIcon(icon)
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_6 = QtWidgets.QPushButton(self.widget)
            self.pushButton_6.setGeometry(QtCore.QRect(370, 10, 75, 51))
            self.pushButton_6.setStyleSheet("QPushButton{\n"
    "border:0px;\n"
    "\n"
    "\n"
    "}")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_6.setIcon(icon1)
            self.pushButton_6.setObjectName("pushButton_6")
            self.pushButton_3 = QtWidgets.QPushButton(self.widget)
            self.pushButton_3.setGeometry(QtCore.QRect(570, 10, 75, 61))
            self.pushButton_3.setStyleSheet("QPushButton{\n"
    "border:0px;\n"
    "\n"
    "\n"
    "}")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_3.setIcon(icon2)
            self.pushButton_3.setObjectName("pushButton_3")
            self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_8.setGeometry(QtCore.QRect(230, 510, 61, 41))
            self.pushButton_8.setStyleSheet("QPushButton{\n"
    "border:0px;\n"
    "\n"
    "\n"
    "}")
            self.pushButton_8.setText("")
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_8.setIcon(icon3)
            self.pushButton_8.setObjectName("pushButton_8")
            self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_9.setGeometry(QtCore.QRect(290, 510, 61, 41))
            self.pushButton_9.setStyleSheet("QPushButton{\n"
    "border: 0 px;\n"
    "\n"
    "\n"
    "\n"
    "}")
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("smile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_9.setIcon(icon4)
            self.pushButton_9.setObjectName("pushButton_9")
            self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
            self.tabWidget.setGeometry(QtCore.QRect(0, 0, 221, 551))
            self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
            self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.tabWidget.setIconSize(QtCore.QSize(35, 66))
            self.tabWidget.setUsesScrollButtons(False)
            self.tabWidget.setDocumentMode(False)
            self.tabWidget.setTabsClosable(False)
            self.tabWidget.setMovable(False)
            self.tabWidget.setTabBarAutoHide(False)
            self.tabWidget.setObjectName("tabWidget")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.listWidget_2 = QtWidgets.QListWidget(self.tab)
            self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 216, 473))
            self.listWidget_2.setObjectName("listWidget_2")
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("comment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.tab, icon5, "")
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.listWidget = QtWidgets.QListWidget(self.tab_3)
            self.listWidget.setGeometry(QtCore.QRect(0, 0, 216, 473))
            self.listWidget.setObjectName("listWidget")
            self.listWidget.itemClicked.connect(self.onClicked)
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.tab_3, icon6, "")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.pushButton = QtWidgets.QPushButton(self.tab_2)
            self.pushButton.setGeometry(QtCore.QRect(0, 150, 221, 31))
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setBold(True)
            font.setWeight(75)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("QPushButton{\n"
    "border:0 px;\n"
    "}\n"
    ".QPushButton:hover{\n"
    "background-color:rgb(216, 216, 216);\n"
    "}\n"
    "")
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("customer-support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon7)
            self.pushButton.setIconSize(QtCore.QSize(22, 29))
            self.pushButton.setCheckable(False)
            self.pushButton.setChecked(False)
            self.pushButton.setAutoRepeat(False)
            self.pushButton.setAutoExclusive(False)
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
            self.pushButton_2.setGeometry(QtCore.QRect(-6, 182, 231, 31))
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("QPushButton{\n"
    "border:0 px;\n"
    "}\n"
    ".QPushButton:hover{\n"
    "background-color:rgb(216, 216, 216);\n"
    "}\n"
    "")
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("technical-support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_2.setIcon(icon8)
            self.pushButton_2.setIconSize(QtCore.QSize(28, 33))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
            self.pushButton_4.setGeometry(QtCore.QRect(-6, 220, 231, 31))
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_4.setFont(font)
            self.pushButton_4.setStyleSheet("QPushButton{\n"
    "border:0 px;\n"
    "}\n"
    ".QPushButton:hover{\n"
    "background-color:rgb(216, 216, 216);\n"
    "}\n"
    "")
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_4.setIcon(icon9)
            self.pushButton_4.setIconSize(QtCore.QSize(28, 33))
            self.pushButton_4.setObjectName("pushButton_4")
            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.tab_2, icon10, "")
            self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
            self.textEdit.setGeometry(QtCore.QRect(360, 501, 401, 51))
            self.textEdit.setObjectName("textEdit")
            self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_10.setGeometry(QtCore.QRect(770, 506, 41, 41))
            self.pushButton_10.setStyleSheet(".QPushButton{\n"
    "background-color:rgb(85, 0, 255);\n"
    "border-top-left-radius:20%;\n"
    "border-top-right-radius:20%;\n"
    "border-bottom-left-radius:20%;\n"
    "border-bottom-right-radius:20%;\n"
    "\n"
    "\n"
    "}")
            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("paper-plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_10.setIcon(icon11)
            self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
            self.pushButton_10.setObjectName("pushButton_10")
            self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_7.setGeometry(QtCore.QRect(830, 506, 41, 41))
            self.pushButton_7.setStyleSheet(".QPushButton{\n"
    "background-color:rgb(85, 0, 255);\n"
    "border-top-left-radius:20%;\n"
    "border-top-right-radius:20%;\n"
    "border-bottom-left-radius:20%;\n"
    "border-bottom-right-radius:20%;\n"
    "\n"
    "\n"
    "}")
            icon12 = QtGui.QIcon()
            icon12.addPixmap(QtGui.QPixmap("voice-message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_7.setIcon(icon12)
            self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
            self.pushButton_7.setObjectName("pushButton_7")
            self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_11.setGeometry(QtCore.QRect(190, 0, 41, 71))
            self.pushButton_11.setStyleSheet("QPushButton{\n"
    "border:0px;\n"
    "\n"
    "\n"
    "}")
            self.pushButton_11.setIcon(icon1)
            self.pushButton_11.setObjectName("pushButton_11")
            self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.plainTextEdit.setGeometry(QtCore.QRect(220, 80, 658, 421))
            self.plainTextEdit.setReadOnly(True)
            self.plainTextEdit.setObjectName("plainTextEdit")
            self.widget_2 = QtWidgets.QWidget(self.centralwidget)
            self.widget_2.setGeometry(QtCore.QRect(751, -1, 130, 551))
            self.widget_2.setObjectName("widget_2")
            self.label = QtWidgets.QLabel(self.widget_2)
            self.label.setGeometry(QtCore.QRect(26, 170, 61, 21))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.widget_2)
            self.label_2.setGeometry(QtCore.QRect(27, 210, 47, 21))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.widget)
            self.label_3.setGeometry(QtCore.QRect(80, 25, 61, 21))
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(423, 20, 281, 91))
            font = QtGui.QFont()
            font.setPointSize(20)
            self.label_4.setFont(font)
            self.label_4.setAlignment(QtCore.Qt.AlignCenter)
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(474, 120, 181, 41))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_5.setFont(font)
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(270, 238, 211, 181))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_6.setFont(font)
            self.label_6.setPixmap(QtGui.QPixmap("conversation.png"))
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setGeometry(QtCore.QRect(260, 423, 231, 121))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_7.setFont(font)
            self.label_7.setTextFormat(QtCore.Qt.AutoText)
            self.label_7.setScaledContents(False)
            self.label_7.setAlignment(QtCore.Qt.AlignCenter)
            self.label_7.setWordWrap(True)
            self.label_7.setObjectName("label_7")
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setGeometry(QtCore.QRect(226, 172, 651, 61))
            font = QtGui.QFont()
            font.setPointSize(27)
            font.setBold(False)
            font.setUnderline(False)
            font.setWeight(50)
            self.label_8.setFont(font)
            self.label_8.setAlignment(QtCore.Qt.AlignCenter)
            self.label_8.setWordWrap(True)
            self.label_8.setObjectName("label_8")
            self.label_9 = QtWidgets.QLabel(self.centralwidget)
            self.label_9.setGeometry(QtCore.QRect(620, 240, 211, 181))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_9.setFont(font)
            self.label_9.setPixmap(QtGui.QPixmap("call.png"))
            self.label_9.setAlignment(QtCore.Qt.AlignCenter)
            self.label_9.setObjectName("label_9")
            self.label_10 = QtWidgets.QLabel(self.centralwidget)
            self.label_10.setGeometry(QtCore.QRect(616, 432, 221, 111))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_10.setFont(font)
            self.label_10.setAlignment(QtCore.Qt.AlignCenter)
            self.label_10.setObjectName("label_10")
            MainWindow.setCentralWidget(self.centralwidget)
            self.retranslateUi(MainWindow)
            self.tabWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
            self.pushButton_11.clicked.connect(self.add_user)
            self.pushButton_10.clicked.connect(self.conn)
            self.textEdit.setPlaceholderText('write message')
            self.pushButton_3.setCheckable(True)
            self.pushButton_3.clicked.connect(self.show_wid)
            self.widget_2.hide()
            self.label.hide()
            self.label_2.hide()
            self.plainTextEdit.hide()
            self.textEdit.hide()
            self.widget.hide()
            self.pushButton_7.hide()
            self.pushButton_10.hide()
            self.pushButton_9.hide()
            self.pushButton_9.hide()
   def add_user(self):
        global id_button
        global count
        input_box = InputBox()
        input_box.setWindowTitle("InputBox Dialog")
        if input_box.exec_() == QtWidgets.QDialog.Accepted:
            val = input_box.save()
            self.listWidget.addItem(val)
   def onClicked(self, item):
            self.word = item.text()
            self.listWidget_2.addItem(self.word)
            self.listWidget_2.clicked.connect(self.open_chat)
   def conn(self):
         message_send = self.textEdit.toPlainText()
         self.plainTextEdit.appendPlainText(message_send)
         self.textEdit.clear()
   def open_chat(self):
       self.label.show()
       self.label_2.show()
       self.plainTextEdit.show()
       self.textEdit.show()
       self.widget.show()
       self.pushButton_7.show()
       self.pushButton_10.show()
       self.pushButton_9.show()
       self.pushButton_9.show()
       self.label_4.hide()
       self.label_5.hide()
       self.label_6.hide()
       self.label_7.hide()
       self.label_8.hide()
       self.label_9.hide()
       self.label_10.hide()
       self.word1 = self.listWidget_2.currentItem()
       self.label_3.setText(self.word1.text())
   def show_wid(self):
        if self.pushButton_3.isChecked():
            self.widget_2.show()
            self.label.show()
            self.label_2.show()
            self.label_3.setGeometry(QtCore.QRect(80, 25, 61, 21))
            self.pushButton_6.setGeometry(QtCore.QRect(180, 10, 75, 51))
            self.pushButton_5.setGeometry(QtCore.QRect(280, 10, 75, 51))
            self.pushButton_3.setGeometry(QtCore.QRect(380, 10, 75, 51))
            self.widget.setGeometry(QtCore.QRect(240, 0, 511, 80))
            self.plainTextEdit.setGeometry(QtCore.QRect(220, 80, 531, 421))
            self.textEdit.setGeometry(QtCore.QRect(360, 501, 271, 51))
            self.pushButton_10.setGeometry(QtCore.QRect(640, 506, 41, 41))
            self.pushButton_7.setGeometry(QtCore.QRect(690, 506, 41, 41))
        else:
            self.widget_2.hide()
            self.label.hide()
            self.label_2.hide()
            self.label_3.setGeometry(QtCore.QRect(80, 25, 61, 21))
            self.pushButton_6.setGeometry(QtCore.QRect(370, 10, 75, 51))
            self.pushButton_5.setGeometry(QtCore.QRect(470, 10, 75, 51))
            self.pushButton_3.setGeometry(QtCore.QRect(570, 10, 75, 51))
            self.widget.setGeometry(QtCore.QRect(240, 0, 641, 80))
            self.plainTextEdit.setGeometry(QtCore.QRect(220, 80, 658, 421))
            self.textEdit.setGeometry(QtCore.QRect(360, 501, 401, 51))
            self.pushButton_10.setGeometry(QtCore.QRect(770, 506, 41, 41))
            self.pushButton_7.setGeometry(QtCore.QRect(830, 506, 41, 41))
   def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gusmes"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.pushButton_2.setText(_translate("MainWindow", "Support"))
        self.pushButton_4.setText(_translate("MainWindow", "Log Out"))
        self.label.setText(_translate("MainWindow", "number"))
        self.label_2.setText(_translate("MainWindow", "name"))
        self.label_3.setText(_translate("MainWindow", "name"))
        self.label_4.setText(_translate("MainWindow", "Welcome!"))
        self.label_5.setText(_translate("MainWindow", "name"))
        self.label_7.setText(_translate("MainWindow", "Write messages your friends.No limits!!"))
        self.label_8.setText(_translate("MainWindow", "     First you can try:"))
        self.label_10.setText(_translate("MainWindow", "Free calling"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())