from PyQt5 import QtCore, QtGui, QtWidgets
from createelection import Ui_Form
from studentRegister import Students
from register import Register

class Ui_MainWindow(object):
        
    def enterAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
    
    def entercandidate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Register()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def enterstudent(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Students()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 483)
        MainWindow.setStyleSheet("*\n"
"{\n"
"    background-color: grey;\n"
"    color: white;\n"
"    font: bold;\n"
"}\n"
"\n"
"#election\n"
"{\n"
"    color : white;\n"
"    background-color: blue;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"\n"
"#database\n"
"{\n"
"    color : white;\n"
"    background-color: green;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"\n"
"#monitor\n"
"{\n"
"    color : white;\n"
"    background-color: red;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"\n"
"#download\n"
"{\n"
"    color : white;\n"
"    background-color: brown;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"#exit\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font: bold;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(310, 210, 221, 131))
        self.download.setObjectName("download")

        self.monitor = QtWidgets.QPushButton(self.centralwidget)
        self.monitor.setGeometry(QtCore.QRect(30, 210, 221, 131))
        self.monitor.setObjectName("monitor")
        ###
        self.monitor.clicked.connect(self.enterstudent)
        ###
        self.election = QtWidgets.QPushButton(self.centralwidget)
    
        self.election.setGeometry(QtCore.QRect(30, 30, 221, 131))
        self.election.setObjectName("election")
        ####
        self.election.clicked.connect(self.enterAdmin)
        ####
        self.database = QtWidgets.QPushButton(self.centralwidget)
        self.database.setGeometry(QtCore.QRect(310, 30, 221, 131))
        self.database.setObjectName("database")
        ###
        self.database.clicked.connect(self.entercandidate)
        ###
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(430, 372, 101, 31))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 22))
        self.menubar.setObjectName("menubar")
        self.menuADMIN = QtWidgets.QMenu(self.menubar)
        self.menuADMIN.setObjectName("menuADMIN")
        self.menuSTATISTICS = QtWidgets.QMenu(self.menuADMIN)
        self.menuSTATISTICS.setObjectName("menuSTATISTICS")
        self.menuRESULT_CHECK = QtWidgets.QMenu(self.menuADMIN)
        self.menuRESULT_CHECK.setObjectName("menuRESULT_CHECK")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLOGOUT_2 = QtWidgets.QAction(MainWindow)
        self.actionLOGOUT_2.setObjectName("actionLOGOUT_2")
        self.actionLOG = QtWidgets.QAction(MainWindow)
        self.actionLOG.setObjectName("actionLOG")
        self.actionVERIFY_RESULTS = QtWidgets.QAction(MainWindow)
        self.actionVERIFY_RESULTS.setObjectName("actionVERIFY_RESULTS")
        self.actionPUBLISH_RESULTS = QtWidgets.QAction(MainWindow)
        self.actionPUBLISH_RESULTS.setObjectName("actionPUBLISH_RESULTS")
        self.menuSTATISTICS.addSeparator()
        self.menuSTATISTICS.addAction(self.actionLOG)
        self.menuRESULT_CHECK.addAction(self.actionVERIFY_RESULTS)
        self.menuRESULT_CHECK.addAction(self.actionPUBLISH_RESULTS)
        self.menuADMIN.addAction(self.menuRESULT_CHECK.menuAction())
        self.menuADMIN.addAction(self.menuSTATISTICS.menuAction())
        self.menuADMIN.addAction(self.actionLOGOUT_2)
        self.menubar.addAction(self.menuADMIN.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.download.setText(_translate("MainWindow", "CHECK DATABASES"))
        self.monitor.setText(_translate("MainWindow", "REGISTER STUDENT"))
        self.election.setText(_translate("MainWindow", "CREATE ELECTION"))
        self.database.setText(_translate("MainWindow", "ADD CANDIDATE"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.menuADMIN.setTitle(_translate("MainWindow", "ADMIN"))
        self.menuSTATISTICS.setTitle(_translate("MainWindow", "STATISTICS"))
        self.menuRESULT_CHECK.setTitle(_translate("MainWindow", "RESULT CHECK"))
        self.actionLOGOUT_2.setText(_translate("MainWindow", "LOGOUT"))
        self.actionLOG.setText(_translate("MainWindow", "LOG"))
        self.actionVERIFY_RESULTS.setText(_translate("MainWindow", "VERIFY RESULTS"))
        self.actionPUBLISH_RESULTS.setText(_translate("MainWindow", "PUBLISH RESULTS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
