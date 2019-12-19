from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

class Ui_Form(object):
    conn = sqlite3.connect("E-VOTING.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM masterlogin")
    result = cur.fetchall()
    final = list(result)
    #print(final)
    query = final[-1]
    #print(query)
    #result2 = cur.execute("SELECT * FROM registered_voters WHERE EMAIL = ?" ,(query,))
    result2 = cur.execute("SELECT * FROM registered_voters WHERE EMAIL = ? ",(query))
    query2 = result2.fetchall()
    for lists in query2:
        name = lists[0]
        surname = lists[1]
        mat = lists[2]
        school = lists[3]
        email = lists[4]
        print(name,surname,mat,school,email)

    conn.commit()
    conn.close()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 530)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(9, 10, 281, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 261, 51))
        #self.label.setObjectName(name)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 261, 51))
#        self.label_2.setObjectName(surname)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 261, 51))
#        self.label_3.setObjectName(mat)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 261, 51))
#        self.label_4.setObjectName(school)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 261, 51))
#        self.label_5.setObjectName(email)
        self.election1 = QtWidgets.QPushButton(Form)
        self.election1.setGeometry(QtCore.QRect(310, 20, 231, 121))
        self.election1.setObjectName("election1")
        self.election2 = QtWidgets.QPushButton(Form)
        self.election2.setGeometry(QtCore.QRect(580, 20, 241, 121))
        self.election2.setObjectName("election2")
        self.election4 = QtWidgets.QPushButton(Form)
        self.election4.setGeometry(QtCore.QRect(580, 180, 241, 121))
        self.election4.setObjectName("election4")
        self.election3 = QtWidgets.QPushButton(Form)
        self.election3.setGeometry(QtCore.QRect(310, 180, 231, 121))
        self.election3.setObjectName("election3")
        self.election6 = QtWidgets.QPushButton(Form)
        self.election6.setGeometry(QtCore.QRect(580, 340, 241, 111))
        self.election6.setObjectName("election6")
        self.election5 = QtWidgets.QPushButton(Form)
        self.election5.setGeometry(QtCore.QRect(310, 340, 231, 111))
        self.election5.setObjectName("election5")
        self.logout = QtWidgets.QPushButton(Form)
        self.logout.setGeometry(QtCore.QRect(470, 470, 171, 51))
        self.logout.setObjectName("logout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "name"))
        self.label_2.setText(_translate("Form", "school"))
        self.label_3.setText(_translate("Form", "email"))
        self.label_4.setText(_translate("Form", "matnumber"))
        self.label_5.setText(_translate("Form", "address"))
        self.election1.setText(_translate("Form", "pushButton"))
        self.election2.setText(_translate("Form", "pushButton"))
        self.election4.setText(_translate("Form", "PushButton"))
        self.election3.setText(_translate("Form", "PushButton"))
        self.election6.setText(_translate("Form", "PushButton"))
        self.election5.setText(_translate("Form", "PushButton"))
        self.logout.setText(_translate("Form", "LOGOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
