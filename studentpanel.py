from PyQt5 import QtCore, QtGui, QtWidgets
from vote import Vote

class Ui_Form(object):
    
    def entervote(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Vote()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 427)
        Form.setStyleSheet("\n"
"#checkelections\n"
"{\n"
"    background-color: grey;\n"
"    color: white;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#vote\n"
"{\n"
"    background-color: grey;\n"
"    color: white;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#checkresult\n"
"{\n"
"    background-color: grey;\n"
"    color: white;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#logout\n"
"{\n"
"    background-color: white;\n"
"    color: red;\n"
"    font: bold;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 381, 41))
        self.label.setObjectName("label")
        self.checkelections = QtWidgets.QPushButton(Form)
        self.checkelections.setGeometry(QtCore.QRect(80, 60, 281, 91))
        self.checkelections.setObjectName("checkelections")
        self.vote = QtWidgets.QPushButton(Form)
        self.vote.setGeometry(QtCore.QRect(80, 170, 281, 91))
        self.vote.setObjectName("vote")
        ###
        self.vote.clicked.connect(self.entervote)
        ###
        self.checkresult = QtWidgets.QPushButton(Form)
        self.checkresult.setGeometry(QtCore.QRect(80, 280, 281, 91))
        self.checkresult.setObjectName("checkresult")
        self.logout = QtWidgets.QPushButton(Form)
        self.logout.setGeometry(QtCore.QRect(334, 392, 101, 31))
        self.logout.setObjectName("logout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#00007f;\">WELCOME BACK!</span></p></body></html>"))
        self.checkelections.setText(_translate("Form", "CHECK ELECTIONS"))
        self.vote.setText(_translate("Form", "VOTE"))
        self.checkresult.setText(_translate("Form", "CHECK RESULTS"))
        self.logout.setText(_translate("Form", "LOGOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
