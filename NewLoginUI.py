import os
from NewSignupUI import Signup_UI
from PyQt5 import QtCore, QtGui, QtWidgets
from MusicPlayer import Ui_MainWindow

class Login_UI(object):
    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(600, 630)
        Form.move(1200,200)
        Form.setFixedSize(600,635)
        Form.setWindowIcon(QtGui.QIcon("images/login.jpg"))
        Form.setStyleSheet("QPushButton#loginButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#loginButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#loginButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}\n"
"QPushButton#newuserButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#newuserButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#newuserButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}\n"
"QPushButton#guestloginButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#guestloginButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#guestloginButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 651))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 641))
        self.label.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.usernameText = QtWidgets.QLineEdit(self.widget)
        self.usernameText.setGeometry(QtCore.QRect(170, 220, 250, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usernameText.setFont(font)
        self.usernameText.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.usernameText.setText("")
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLineEdit(self.widget)
        self.passwordText.setGeometry(QtCore.QRect(170, 310, 250, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordText.setFont(font)
        self.passwordText.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordText.setObjectName("passwordText")
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setGeometry(QtCore.QRect(170, 400, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.newuserButton = QtWidgets.QPushButton(self.widget)
        self.newuserButton.setGeometry(QtCore.QRect(170, 470, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newuserButton.setFont(font)
        self.newuserButton.setObjectName("newuserButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 201, 171))
        font = QtGui.QFont()
        font.setPointSize(120)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgba(0,125,200,255)\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.guestloginButton = QtWidgets.QPushButton(self.widget)
        self.guestloginButton.setGeometry(QtCore.QRect(390, 530, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.guestloginButton.setFont(font)
        self.guestloginButton.setObjectName("guestloginButton")
        self.statusLabel = QtWidgets.QLabel(self.widget)
        self.statusLabel.setGeometry(QtCore.QRect(200, 570, 191, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("color: rgb(232, 232, 232);")
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")

        self.loginButton.clicked.connect(self.login)
        self.newuserButton.clicked.connect(self.new)
        self.guestloginButton.clicked.connect(self.guest)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign In"))
        self.usernameText.setPlaceholderText(_translate("Form", "  User Name"))
        self.passwordText.setPlaceholderText(_translate("Form", "  Password"))
        self.loginButton.setText(_translate("Form", "Log In"))
        self.newuserButton.setText(_translate("Form", "New User ?"))
        self.label_2.setText(_translate("Form", "♫"))
        self.guestloginButton.setText(_translate("Form", "Guest Login"))

    def login(self):
        self.username = self.usernameText.text()
        self.password = self.passwordText.text()

        if(self.username == "" or self.password==""):
            self.statusLabel.setText("Invalid Details")

        else:
            if self.username in os.listdir("Users/"):
                file = open("Users/"+self.username+"/login").readlines()
                if self.password in file:
                    self.statusLabel.setText("Login Successful")
                    self.loginSuccess(0)

                else:
                    self.statusLabel.setText("Wrong Password")

            else:
                self.statusLabel.setText("User Not Found")

    def guest(self):
        self.statusLabel.setText("     Guest Login")
        self.loginSuccess(1)


    def new(self):
        self.signup = QtWidgets.QWidget()
        self.ui = Signup_UI()
        self.ui.setupUi(self.signup)
        self.signup.setWindowModality(QtCore.Qt.ApplicationModal)
        self.signup.show()

    def loginSuccess(self,flag):
        self.window = QtWidgets.QMainWindow()
        self.musicUI = Ui_MainWindow()

        if(flag==1):
            self.musicUI.guestLogin=True

        else:
            self.musicUI.userid=self.username

        self.musicUI.setupUi(self.window)
        self.musicUI.events()
        QtCore.QTimer.singleShot(1000,self.main.close)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
