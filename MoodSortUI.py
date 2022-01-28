from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MoodUI(object):
    def setupUi(self, MoodUI):
        MoodUI.setObjectName("MoodUI")
        MoodUI.resize(406, 223)
        MoodUI.setWindowIcon(QtGui.QIcon("images/sort.png"))
        self.label = QtWidgets.QLabel(MoodUI)
        self.label.setGeometry(QtCore.QRect(50, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 18pt \"Nirmala UI Semilight\";")
        self.label.setObjectName("label")
        self.moodBox = QtWidgets.QComboBox(MoodUI)
        self.moodBox.setGeometry(QtCore.QRect(100, 80, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.moodBox.setFont(font)
        self.moodBox.setStyleSheet("\n"
"font: 16pt \"Sitka Heading\";")
        self.moodBox.setObjectName("moodBox")
        self.moodBox.addItem("")
        self.moodBox.addItem("")
        self.moodBox.addItem("")
        self.moodBox.addItem("")
        self.moodBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(MoodUI)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MoodUI)
        QtCore.QMetaObject.connectSlotsByName(MoodUI)

    def retranslateUi(self, MoodUI):
        _translate = QtCore.QCoreApplication.translate
        MoodUI.setWindowTitle(_translate("MoodUI", "Choose Mood"))
        self.label.setText(_translate("MoodUI", "How are you feeling??"))
        self.moodBox.setItemText(0, _translate("MoodUI", "Happy"))
        self.moodBox.setItemText(1, _translate("MoodUI", "Sorrow"))
        self.moodBox.setItemText(2, _translate("MoodUI", "Energetic"))
        self.moodBox.setItemText(3, _translate("MoodUI", "Calm"))
        self.moodBox.setItemText(4, _translate("MoodUI", "Romantic"))
        self.pushButton.setText(_translate("MoodUI", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MoodUI = QtWidgets.QDialog()
    ui = Ui_MoodUI()
    ui.setupUi(MoodUI)
    MoodUI.show()
    sys.exit(app.exec_())
