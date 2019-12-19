from PyQt5 import QtCore, QtGui, QtWidgets
from candidatepopup import CandidatePopup
import sqlite3

def createDb():
    con = sqlite3.connect('E-VOTING.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS candidates(MAT INTEGER,NAME TEXT,SCHOOL TEXT,MAJOR TEXT,CONTACT INTEGER,EMAIL TEXT,ADDRESS TEXT,POSITION TEXT)")
    con.commit()
    con.close()
#createDb()
    
class Register(object):
    
    def popup(self):  
        self.window = QtWidgets.QMainWindow()
        self.ui = CandidatePopup()
        self.ui.setupUi(self.window)
        self.window.show()
        #MainWindow.hide()
        
    def candidate(self):
        mat =   self.matnumber.text()
        name = self.firstname.text()
        school = self.lastname.text()
        major = self.major.text()
        contact = self.contact.text()
        email = self.email.text()
        address = self.address.text()
        position =  self.position.currentText()
        
        try:
            con = sqlite3.connect("E-VOTING.db")
            cur = con.cursor()
            cur.execute("INSERT INTO candidates VALUES(?,?,?,?,?,?,?,?)",(mat,name,school,major,contact,email,address,position))
            con.commit()
            con.close()
        except:
            print("Error in the database!!!!")
        self.popup()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 781, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(90, 10, 591, 121))
        self.label_9.setObjectName("label_9")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 781, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.firstname = QtWidgets.QLineEdit(self.frame_2)
        self.firstname.setGeometry(QtCore.QRect(160, 30, 181, 51))
        self.firstname.setObjectName("firstname")
        self.matnumber = QtWidgets.QLineEdit(self.frame_2)
        self.matnumber.setGeometry(QtCore.QRect(570, 110, 181, 51))
        self.matnumber.setObjectName("matnumber")
        self.email = QtWidgets.QLineEdit(self.frame_2)
        self.email.setGeometry(QtCore.QRect(570, 190, 181, 51))
        self.email.setObjectName("email")
        self.lastname = QtWidgets.QLineEdit(self.frame_2)
        self.lastname.setGeometry(QtCore.QRect(160, 110, 181, 51))
        self.lastname.setObjectName("lastname")
        self.major = QtWidgets.QLineEdit(self.frame_2)
        self.major.setGeometry(QtCore.QRect(570, 30, 181, 51))
        self.major.setObjectName("major")
        self.address = QtWidgets.QLineEdit(self.frame_2)
        self.address.setGeometry(QtCore.QRect(160, 270, 181, 51))
        self.address.setObjectName("address")
        self.contact = QtWidgets.QLineEdit(self.frame_2)
        self.contact.setGeometry(QtCore.QRect(160, 190, 181, 51))
        self.contact.setObjectName("contact")
        self.addcandidate = QtWidgets.QPushButton(self.frame_2)
        self.addcandidate.setGeometry(QtCore.QRect(300, 350, 131, 31))
        self.addcandidate.setStyleSheet("font: bold;\ncolor: blue;")
        self.addcandidate.setObjectName("addcandidate")
##        self.viewList = QtWidgets.QPushButton(self.frame_2)
##        self.viewList.setGeometry(QtCore.QRect(150, 350, 131, 31))
##        self.viewList.setStyleSheet("font: bold;\ncolor: blue;")
##        self.viewList.setObjectName("viewList")
        ###
        self.addcandidate.clicked.connect(self.candidate)
        ###
        self.exit = QtWidgets.QPushButton(self.frame_2)
        self.exit.setGeometry(QtCore.QRect(470, 350, 101, 31))
        self.exit.setStyleSheet("color: blue;\n"
"font: bold;")
        self.exit.setObjectName("exit")
        self.position = QtWidgets.QComboBox(self.frame_2)
        self.position.setGeometry(QtCore.QRect(570, 270, 181, 51))
        self.position.setObjectName("position")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.position.addItem("")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 121, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 121, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 121, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(430, 30, 121, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(420, 110, 131, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(430, 190, 121, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(430, 270, 121, 41))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView_Tables = QtWidgets.QMenu(self.menubar)
        self.menuView_Tables.setObjectName("menuView_Tables")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCandidate_Table = QtWidgets.QAction(MainWindow)
        self.actionCandidate_Table.setObjectName("actionCandidate_Table")
        self.actionPresident_Table = QtWidgets.QAction(MainWindow)
        self.actionPresident_Table.setObjectName("actionPresident_Table")
        self.actionVice_President_Table = QtWidgets.QAction(MainWindow)
        self.actionVice_President_Table.setObjectName("actionVice_President_Table")
        self.actionFinance_Minister = QtWidgets.QAction(MainWindow)
        self.actionFinance_Minister.setObjectName("actionFinance_Minister")
        self.actionWelfare_MInister = QtWidgets.QAction(MainWindow)
        self.actionWelfare_MInister.setObjectName("actionWelfare_MInister")
        self.actionIpro = QtWidgets.QAction(MainWindow)
        self.actionIpro.setObjectName("actionIpro")
        self.actionIpro_2 = QtWidgets.QAction(MainWindow)
        self.actionIpro_2.setObjectName("actionIpro_2")
        self.menuView_Tables.addAction(self.actionCandidate_Table)
        self.menuView_Tables.addAction(self.actionPresident_Table)
        self.menuView_Tables.addAction(self.actionVice_President_Table)
        self.menuView_Tables.addAction(self.actionFinance_Minister)
        self.menuView_Tables.addAction(self.actionWelfare_MInister)
        self.menuView_Tables.addAction(self.actionIpro)
        self.menuView_Tables.addAction(self.actionIpro_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView_Tables.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UTG E-VOTING SYSTEM"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#204a87;\">University Of The Gambia</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#204a87;\">Voting System </span></p></body></html>"))
        self.addcandidate.setText(_translate("MainWindow", "REGISTER"))
##        self.viewList.setText(_translate("MainWindow", "VIEW LIST"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.position.setItemText(0, _translate("MainWindow", "PRESIDENT"))
        self.position.setItemText(1, _translate("MainWindow", "VICE PRESIDENT"))
        self.position.setItemText(2, _translate("MainWindow", "FINANCE MINISTER"))
        self.position.setItemText(3, _translate("MainWindow", "WELFARE MINISTER"))
        self.position.setItemText(4, _translate("MainWindow", "SECRETARY GENERAL"))
        self.position.setItemText(5, _translate("MainWindow", "IPRO"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">FULL NAME</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">SCHOOL</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">CONTACT</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">ADDRESS</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">MAJOR</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">MAT NUMBER</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">EMAIL</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#204a87;\">POSITION</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView_Tables.setTitle(_translate("MainWindow", "View Tables"))
        self.actionCandidate_Table.setText(_translate("MainWindow", "Candidate Table"))
        self.actionPresident_Table.setText(_translate("MainWindow", "President Table"))
        self.actionVice_President_Table.setText(_translate("MainWindow", "Vice-President Table"))
        self.actionFinance_Minister.setText(_translate("MainWindow", "Finance Minister"))
        self.actionWelfare_MInister.setText(_translate("MainWindow", "Welfare MInister"))
        self.actionIpro.setText(_translate("MainWindow", "Secretary General"))
        self.actionIpro_2.setText(_translate("MainWindow", "Ipro"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Register()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())