from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("E-VOTING.db")
cur = conn.cursor()
    
verify = cur.execute("SELECT USERNAME FROM activelogins")
username = verify.fetchall()
lists = list(username)
check = lists[-1]

verify2 = cur.execute("SELECT * FROM student WHERE EMAIL = ?",(check))

result = verify.fetchall()
for x in result:
    print(x)


#printout = cur.execute("SELECT * FROM registered_voters WHERE EMAIL = ?",(username))
#    
#for details in printout:
#    fname = details[0]
#    fsurname = details[1]
#    fmat = details[2]
#    fschool = details[3]
#    femail = details[4]
#        
#    #print(name,surname)

    
conn.commit()
conn.close()



class Ui_MainWindow(object):
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 564)
        MainWindow.setStyleSheet("\n"
"\n"
"#frame2\n"
"{\n"
"    background: grey;\n"
"}\n"
"#line1\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line2\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line3\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line4\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line5\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: red;\n"
"}\n"
"#line6\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: red;\n"
"}\n"
"#election1\n"
"{\n"
"    background-color: white;\n"
"    color: red;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election2\n"
"{\n"
"    background-color: black;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election3\n"
"{\n"
"    background-color: yellow;\n"
"    color: red;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election4\n"
"{\n"
"    background-color: violet;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election5\n"
"{\n"
"    background-color: pink;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election6\n"
"{\n"
"    background-color: brown;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election7\n"
"{\n"
"    background-color: blue;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election8\n"
"{\n"
"    background-color: green;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(240, -1, 431, 531))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.election1 = QtWidgets.QPushButton(self.frame2)
        self.election1.setGeometry(QtCore.QRect(10, 40, 191, 91))
        self.election1.setObjectName("election1")
        self.election2 = QtWidgets.QPushButton(self.frame2)
        self.election2.setGeometry(QtCore.QRect(230, 40, 191, 91))
        self.election2.setObjectName("election2")
        self.election3 = QtWidgets.QPushButton(self.frame2)
        self.election3.setGeometry(QtCore.QRect(10, 170, 191, 91))
        self.election3.setObjectName("election3")
        self.election4 = QtWidgets.QPushButton(self.frame2)
        self.election4.setGeometry(QtCore.QRect(230, 170, 191, 91))
        self.election4.setObjectName("election4")
        self.election5 = QtWidgets.QPushButton(self.frame2)
        self.election5.setGeometry(QtCore.QRect(10, 300, 191, 91))
        self.election5.setObjectName("election5")
        self.election6 = QtWidgets.QPushButton(self.frame2)
        self.election6.setGeometry(QtCore.QRect(230, 300, 191, 91))
        self.election6.setObjectName("election6")
        self.election7 = QtWidgets.QPushButton(self.frame2)
        self.election7.setGeometry(QtCore.QRect(10, 420, 191, 81))
        self.election7.setObjectName("election7")
        self.election8 = QtWidgets.QPushButton(self.frame2)
        self.election8.setGeometry(QtCore.QRect(230, 420, 191, 81))
        self.election8.setObjectName("election8")
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(80, 10, 241, 16))
        self.label.setObjectName("label")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(10, 20, 221, 41))
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(10, 60, 221, 41))
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(10, 100, 221, 41))
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(10, 140, 221, 41))
        self.line4.setObjectName("line4")
        self.line5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line5.setGeometry(QtCore.QRect(10, 180, 221, 41))
        self.line5.setObjectName("line5")
        self.line6 = QtWidgets.QLineEdit(self.centralwidget)
        self.line6.setGeometry(QtCore.QRect(10, 220, 221, 41))
        self.line6.setObjectName("line6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        self.menuCHECK_POLLS = QtWidgets.QMenu(self.menuMENU)
        self.menuCHECK_POLLS.setObjectName("menuCHECK_POLLS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLOGOUT = QtWidgets.QAction(MainWindow)
        self.actionLOGOUT.setObjectName("actionLOGOUT")
        self.actionPREVIOUS_RESULTS = QtWidgets.QAction(MainWindow)
        self.actionPREVIOUS_RESULTS.setObjectName("actionPREVIOUS_RESULTS")
        self.actionCURRENT_POLLS = QtWidgets.QAction(MainWindow)
        self.actionCURRENT_POLLS.setObjectName("actionCURRENT_POLLS")
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.menuCHECK_POLLS.addAction(self.actionCURRENT_POLLS)
        self.menuCHECK_POLLS.addAction(self.actionPREVIOUS_RESULTS)
        self.menuMENU.addAction(self.menuCHECK_POLLS.menuAction())
        self.menuMENU.addAction(self.actionLOGOUT)
        self.menuMENU.addAction(self.actionEXIT)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
#        ###
#        self.line1.setText(fname.upper())
#        self.line2.setText(fsurname.upper())
#        self.line3.setText(fmat.upper())
#        self.line4.setText(fschool.upper())
#        self.line5.setText(femail.upper())
#        ###

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.election1.setText(_translate("MainWindow", "PushButton"))
        self.election2.setText(_translate("MainWindow", "PushButton"))
        self.election3.setText(_translate("MainWindow", "PushButton"))
        self.election4.setText(_translate("MainWindow", "PushButton"))
        self.election5.setText(_translate("MainWindow", "PushButton"))
        self.election6.setText(_translate("MainWindow", "PushButton"))
        self.election7.setText(_translate("MainWindow", "PushButton"))
        self.election8.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"> CURRENT ELECTIONS</span></p></body></html>"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.menuCHECK_POLLS.setTitle(_translate("MainWindow", "CHECK POLLS"))
        self.actionLOGOUT.setText(_translate("MainWindow", "LOGOUT"))
        self.actionPREVIOUS_RESULTS.setText(_translate("MainWindow", "PREVIOUS RESULTS"))
        self.actionCURRENT_POLLS.setText(_translate("MainWindow", "CURRENT POLLS"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
