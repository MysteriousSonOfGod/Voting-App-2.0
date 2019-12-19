from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Form(object):

    def newElection(self):
        names = self.lineEdit.text()
        dates = self.dateEdit.text()
        association = self.comboBox.currentText()
        candidates = self.spinBox.value()
        
        conn = sqlite3.connect("E-VOTING.db")
        cur = conn.cursor()

        cur.execute("INSERT INTO election VALUES(?,?,?,?)",(names,dates,association,candidates))
        conn.commit()
        conn.close()

    
    def enterAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(477, 398)
        Form.setStyleSheet("\n"
"#back\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font: bold;\n"
"}\n"
"\n"
"#create\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font: bold;\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 70, 191, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 70, 161, 41))
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(220, 140, 191, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(220, 210, 191, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 161, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 151, 41))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(220, 280, 191, 41))
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 290, 151, 41))
        self.label_4.setObjectName("label_4")
        self.create = QtWidgets.QPushButton(Form)
        self.create.setGeometry(QtCore.QRect(250, 350, 141, 41))
        self.create.setObjectName("create")

        ####
        self.create.clicked.connect(self.newElection)
        ####

        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(70, 350, 141, 41))
        self.back.setObjectName("back")

        ####
        self.back.clicked.connect(self.enterAdmin)
        ####
        
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 351, 41))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">ELECTION NAME</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "UTGSU"))
        self.comboBox.setItemText(1, _translate("Form", "SOSHA"))
        self.comboBox.setItemText(2, _translate("Form", "BPA"))
        self.comboBox.setItemText(3, _translate("Form", "LSA"))
        self.comboBox.setItemText(4, _translate("Form", "ITCA"))
        self.comboBox.setItemText(5, _translate("Form", "SSA"))
        self.comboBox.setItemText(6, _translate("Form", "SAPEH"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">ELECTION DATE</span></p><p><span style=\" color:#00007f;\"><br/></span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">ASSOICIATION</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">CANDIDATES</span></p><p><span style=\" color:#00007f;\"><br/></span></p></body></html>"))
        self.create.setText(_translate("Form", "CREATE ELECTION"))
        self.back.setText(_translate("Form", "ADMIN PANEL"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#00007f;\">CREATE ELECTION</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
