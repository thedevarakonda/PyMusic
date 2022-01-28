from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Signup_UI(object):
    def setupUi(self, Form):
        self.win=Form
        Form.setObjectName("Form")
        Form.setFixedSize(498,510)
        Form.move(600,200)
        Form.setWindowIcon(QtGui.QIcon("images/newuser.png"))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        Form.setFont(font)
        Form.setStyleSheet("QPushButton#signupButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#signupButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#signupButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}\n"
"\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 531))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 521))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.label.setObjectName("label")
        self.usernameText = QtWidgets.QLineEdit(self.widget)
        self.usernameText.setGeometry(QtCore.QRect(120, 220, 250, 30))
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
        self.passwordText.setGeometry(QtCore.QRect(120, 300, 250, 30))
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
        self.signupButton = QtWidgets.QPushButton(self.widget)
        self.signupButton.setGeometry(QtCore.QRect(120, 370, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signupButton.setFont(font)
        self.signupButton.setObjectName("signupButton")
        self.iconLabel = QtWidgets.QLabel(self.widget)
        self.iconLabel.setGeometry(QtCore.QRect(140, 30, 201, 171))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.iconLabel.setFont(font)
        self.iconLabel.setStyleSheet("color: rgba(0,125,200,255)\n"
"")
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.statusLabel = QtWidgets.QLabel(self.widget)
        self.statusLabel.setGeometry(QtCore.QRect(130, 450, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("color: rgb(232, 232, 232);")
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.signupButton.clicked.connect(self.signup)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))
        self.usernameText.setPlaceholderText(_translate("Form", "  User Name"))
        self.passwordText.setPlaceholderText(_translate("Form", "  Password"))
        self.signupButton.setText(_translate("Form", "Sign Up !"))
        self.iconLabel.setText(_translate("Form", ""))

    def signup(self):

            self.username = self.usernameText.text()
            self.password = self.passwordText.text()

            if (self.username == "" or self.password == ""):
                    self.statusLabel.setText("     Invalid Details")

            else:
                    if self.username in os.listdir("Users/"):
                            self.statusLabel.setText("Username already exists")

                    else:
                            os.mkdir("Users/" + self.username)
                            os.mkdir("Users/" + self.username + "/Downloads")
                            os.mkdir("Users/" + self.username + "/Playlists")
                            file = open("Users/" + self.username + "/login", "w")
                            file.write(self.username + "\n" + self.password)
                            file.close()
                            self.statusLabel.setText("Registration Success")
                            QtCore.QTimer.singleShot(1000, self.win.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Signup_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
