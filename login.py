from PyQt5 import QtCore, QtGui, QtWidgets
from adminpanel import Ui_MainWindow

class Ui_Form(object):

    def enterAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 640)
        Form.setStyleSheet("*{\n"
"    font-family: century gothic;\n"
"    font-size: 30px;\n"
"    color: white;\n"
"}\n"
"QFrame\n"
"{\n"
"    background-color: rgba(0,0,0,15);\n"
"    border-radius: 15px;\n"
"}\n"
"#Form\n"
"{\n"
"    background: #333;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color: white;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background: blue;\n"
"    color: white;\n"
"}\n"
"\n"
"#username\n"
"{\n"
"    background : transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    border-bottom: 1px solid white;\n"
"}\n"
"\n"
"#password\n"
"{\n"
"    background : transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    border-bottom: 1px solid white;\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(150, 80, 481, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 60, 291, 41))
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(20, 190, 411, 51))
        self.username.setInputMask("")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(30, 300, 421, 51))
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 390, 291, 61))
        self.pushButton.setObjectName("pushButton")
        
        ####
        
        user = self.username.text()
        passw = self.password.text()
        
        def check(self):
            if user == "admin":
                self.enterAdmin()
                
            elif user = "student":
                pass
            else:
                pass
        
        self.pushButton.clicked.connect(self.enterAdmin)

        ####
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 291, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 291, 41))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "WELCOME BACK"))
        self.username.setPlaceholderText(_translate("Form", "xy2121211@utg.edu.gm"))
        self.password.setPlaceholderText(_translate("Form", "**********"))
        self.pushButton.setText(_translate("Form", "LOGIN"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
