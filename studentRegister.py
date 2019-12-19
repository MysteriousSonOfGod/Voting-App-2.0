from PyQt5 import QtCore, QtGui, QtWidgets
#from studentpopup import StudentPopup
import sqlite3

def createDb():
    con = sqlite3.connect('E-VOTING.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(MAT INTEGER,NAME TEXT,SURNAME TEXT,SCHOOL TEXT,EMAIL TEXT,CONTACT INTEGER)")
    con.commit()
    con.close()
#createDb()

class Students(object):
    
    def registeredPopup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = StudentPopup()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
            
    def store(self):
        mat = self.mat.text()
        name = self.name.text()
        surname = self.mat.text()
        school = self.school.currentText()
        email = self.email.text()
        contact = self.contact.text()    
        try:
            conn = sqlite3.connect("E-VOTING.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO students VALUES(?,?,?,?,?,?)",(mat,name,surname,school,email,contact))
            conn.commit()
            conn.close()
            self.registeredPopup()    

        except:
            print("ERROR ESTABLISHING DATABASE CONNECTION!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 771, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 771, 61))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 119, 771, 451))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.name = QtWidgets.QLineEdit(self.frame_2)
        self.name.setGeometry(QtCore.QRect(130, 100, 201, 51))
        self.name.setObjectName("name")
        self.mat = QtWidgets.QLineEdit(self.frame_2)
        self.mat.setGeometry(QtCore.QRect(130, 200, 201, 51))
        self.mat.setObjectName("mat")
        self.contact = QtWidgets.QLineEdit(self.frame_2)
        self.contact.setGeometry(QtCore.QRect(520, 200, 231, 51))
        self.contact.setObjectName("contact")
        self.email = QtWidgets.QLineEdit(self.frame_2)
        self.email.setGeometry(QtCore.QRect(130, 300, 201, 51))
        self.email.setObjectName("email")
        self.surname = QtWidgets.QLineEdit(self.frame_2)
        self.surname.setGeometry(QtCore.QRect(520, 100, 231, 51))
        self.surname.setObjectName("surname")
        self.school = QtWidgets.QComboBox(self.frame_2)
        self.school.setGeometry(QtCore.QRect(520, 300, 231, 51))
        self.school.setObjectName("school")
        self.school.addItem("")
        self.school.addItem("")
        self.school.addItem("")
        self.school.addItem("")
        self.school.addItem("")
        self.school.addItem("")
        self.school.addItem("")
        self.school.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 91, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 91, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 91, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(380, 100, 141, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(380, 200, 141, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(390, 300, 131, 51))
        self.label_7.setObjectName("label_7")
        self.save = QtWidgets.QPushButton(self.frame_2)
        self.save.setGeometry(QtCore.QRect(240, 394, 141, 41))
        self.save.setStyleSheet("color: blue;\n"
"font: bold ;\n"
"font-size: 20px;")
        self.save.setObjectName("save")
        ###
        self.save.clicked.connect(self.store)
        ###
        self.exit = QtWidgets.QPushButton(self.frame_2)
        self.exit.setGeometry(QtCore.QRect(510, 394, 121, 41))
        self.exit.setStyleSheet("color: blue;\n"
"font: bold;\n"
"font-size: 20px;")
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UTGSU E-VOTING SYSTEM"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#204a87;\">REGISTER STUDENT</span></p></body></html>"))
        self.school.setItemText(0, _translate("MainWindow", "BPA"))
        self.school.setItemText(1, _translate("MainWindow", "LAW"))
        self.school.setItemText(2, _translate("MainWindow", "SOSHA"))
        self.school.setItemText(3, _translate("MainWindow", "SSA"))
        self.school.setItemText(4, _translate("MainWindow", "ICT"))
        self.school.setItemText(5, _translate("MainWindow", "MEDICINE"))
        self.school.setItemText(6, _translate("MainWindow", "AGRICULTURE"))
        self.school.setItemText(7, _translate("MainWindow", "JOURNALISM"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#204a87;\">NAME</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#204a87;\">MAT</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#204a87;\">EMAIL</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#204a87;\">SURNAME</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#204a87;\">CONTACT</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#204a87;\">SCHOOL</span></p></body></html>"))
        self.save.setText(_translate("MainWindow", "REGISTER"))
        self.exit.setText(_translate("MainWindow", "EXIT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Students()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
