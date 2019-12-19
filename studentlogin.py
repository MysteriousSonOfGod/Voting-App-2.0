from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from availableelection import Ui_Form

class Ui_Form(object):
    
#    def enterElection(self):
#        self.window = QtWidgets.QMainWindow()
#        self.ui = Ui_Form()
#        self.ui.setupUi(self.window)
#        self.window.show()
#        MainWindow.hide()    
    
    def logins(self):
        username = self.username.text()
        password = self.password.text()
        conn = sqlite3.connect("E-VOTING.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO masterlogin VALUES(?)",(username,))
        print("New login")
        conn.commit()
        conn.close()
                
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 356)
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(120, 100, 251, 51))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(120, 210, 251, 51))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 60, 251, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 251, 41))
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(200, 300, 89, 41))
        self.login.setObjectName("login")
        
        ####
        self.login.clicked.connect(self.logins)
        ####
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "USERNAME"))
        self.label_2.setText(_translate("Form", "PASSWORD"))
        self.login.setText(_translate("Form", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
