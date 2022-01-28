from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Actors(object):
    def setupUi(self, Actors):
        Actors.setObjectName("Actors")
        Actors.resize(435, 217)
        Actors.setWindowIcon(QtGui.QIcon("images/sort.png"))
        self.actorsList = QtWidgets.QComboBox(Actors)
        self.actorsList.setGeometry(QtCore.QRect(110, 100, 171, 31))
        self.actorsList.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.actorsList.setObjectName("actorsList")
        self.actorsList.addItem("")
        self.actorsList.addItem("")
        self.actorsList.addItem("")
        self.actorsList.addItem("")
        self.actorsList.addItem("")
        self.submitButton = QtWidgets.QPushButton(Actors)
        self.submitButton.setGeometry(QtCore.QRect(150, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"Microsoft YaHei UI\";")
        self.submitButton.setObjectName("submitButton")
        self.actorLabel = QtWidgets.QLabel(Actors)
        self.actorLabel.setGeometry(QtCore.QRect(30, 50, 171, 31))
        self.actorLabel.setStyleSheet("font: 14pt \"MS Reference Sans Serif\";")
        self.actorLabel.setObjectName("actorLabel")

        self.retranslateUi(Actors)
        QtCore.QMetaObject.connectSlotsByName(Actors)

    def retranslateUi(self, Actors):
        _translate = QtCore.QCoreApplication.translate
        Actors.setWindowTitle(_translate("Actors", "Sort by Actors"))
        self.actorsList.setItemText(0, _translate("Actors", "Mahesh Babu"))
        self.actorsList.setItemText(1, _translate("Actors", "Vijay Devarkonda"))
        self.actorsList.setItemText(2, _translate("Actors", "Pawan Kalyan"))
        self.actorsList.setItemText(3, _translate("Actors", "Allu Arjun"))
        self.actorsList.setItemText(4, _translate("Actors", "Prabhas"))
        self.submitButton.setText(_translate("Actors", "Select"))
        self.actorLabel.setText(_translate("Actors", "Choose an Actor: "))

