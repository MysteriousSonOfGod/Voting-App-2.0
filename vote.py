from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from votepopup import Voted


def createDatabase():
    con = sqlite3.connect("E-VOTING.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS votes(NAME TEXT,SURNAME TEXT,PRESIDENT TEXT,VICE_PRESIDENT TEXT,FINANCE_MINISTER TEXT,WELFARE_MINISTER TEXT,SECRETARY TEXT,IPRO TEXT)")
    con.commit()
    con.close()


# createDatabase()

class Vote(object):

    def votedPopup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Voted()
        self.ui.setupUi(self.window)
        self.window.show()
        # MainWindow.hide()

    def viewCandidate(self):
        con = sqlite3.connect("E-VOTING.db")
        cur = con.cursor()
        cur.execute("SELECT  POSITION FROM candidates ")
        con.commit()
        con.close()

    ###Mthod to enter data into database when the vote is clicked
    def voteCast(self):
        name = self.firstname.text()
        surname = self.lastname.text()
        president = self.president.currentText()
        vice = self.vicepresident.currentText()
        finance = self.financeminister.currentText()
        welfare = self.welfareminister.currentText()
        secretary = self.secretary.currentText()
        ipro = self.ipro.currentText()

        try:
            con = sqlite3.connect("E-VOTING.db")
            cur = con.cursor()
            cur.execute("INSERT INTO votes VALUES(?,?,?,?,?,?,?,?) ",
                        (name, surname, president, vice, finance, welfare, secretary, ipro))
            con.commit()
            con.close()
        except:
            print("ERROR ESTABLISHING CONNECTION TO DATABASE!")
        self.votedPopup()

    ###Method to exit when the exit button is clicked
    def exits(self):
        exit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 9, 841, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lastname = QtWidgets.QLineEdit(self.frame)
        self.lastname.setGeometry(QtCore.QRect(580, 20, 211, 51))
        self.lastname.setObjectName("lastname")
        self.firstname = QtWidgets.QLineEdit(self.frame)
        self.firstname.setGeometry(QtCore.QRect(180, 20, 211, 51))
        self.firstname.setObjectName("firstname")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 26, 131, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(450, 20, 131, 51))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 109, 701, 501))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 20, 331, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.president = QtWidgets.QComboBox(self.frame_3)
        self.president.setGeometry(QtCore.QRect(150, 10, 171, 41))
        self.president.setObjectName("president")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(6, 6, 141, 51))
        self.label_3.setObjectName("label_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(370, 20, 331, 61))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.welfareminister = QtWidgets.QComboBox(self.frame_6)
        self.welfareminister.setGeometry(QtCore.QRect(150, 10, 171, 41))
        self.welfareminister.setObjectName("welfareminister")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(60, 40, 141, 61))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 141, 61))
        self.label_11.setObjectName("label_11")
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setGeometry(QtCore.QRect(20, 180, 331, 61))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_12)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 60, 171, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.vicepresident = QtWidgets.QComboBox(self.frame_12)
        self.vicepresident.setGeometry(QtCore.QRect(150, 10, 171, 41))
        self.vicepresident.setObjectName("vicepresident")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 141, 61))
        self.label_4.setObjectName("label_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(370, 180, 331, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.secretary = QtWidgets.QComboBox(self.frame_4)
        self.secretary.setGeometry(QtCore.QRect(150, 10, 171, 41))
        self.secretary.setObjectName("secretary")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 141, 61))
        self.label_7.setObjectName("label_7")
        self.financeministerLine = QtWidgets.QLineEdit(self.frame_2)
        self.financeministerLine.setGeometry(QtCore.QRect(20, 420, 331, 61))
        self.financeministerLine.setObjectName("financeministerLine")
        self.iproLine = QtWidgets.QLineEdit(self.frame_2)
        self.iproLine.setGeometry(QtCore.QRect(370, 420, 331, 61))
        self.iproLine.setObjectName("iproLine")
        self.welfareministerLine = QtWidgets.QLineEdit(self.frame_2)
        self.welfareministerLine.setGeometry(QtCore.QRect(370, 100, 331, 61))
        self.welfareministerLine.setObjectName("welfareministerLine")
        self.presidentLine = QtWidgets.QLineEdit(self.frame_2)
        self.presidentLine.setGeometry(QtCore.QRect(20, 100, 331, 61))
        self.presidentLine.setObjectName("presidentLine")

        ##
        # v = self.president.currentText()
        # self.iproLine.setText(self.president.currentText())
        # x = result
        # y = self.vicepresidentLine(x)
        ##

        self.vicepresidentLine = QtWidgets.QLineEdit(self.frame_2)
        self.vicepresidentLine.setGeometry(QtCore.QRect(20, 260, 331, 61))
        self.vicepresidentLine.setObjectName("vicepresidentLine")
        self.secretaryLine = QtWidgets.QLineEdit(self.frame_2)
        self.secretaryLine.setGeometry(QtCore.QRect(370, 260, 331, 61))
        self.secretaryLine.setObjectName("secretaryLine")

        #######
        self.presidentLine.setReadOnly(True)
        self.vicepresidentLine.setReadOnly(True)
        self.financeministerLine.setReadOnly(True)
        self.welfareministerLine.setReadOnly(True)
        self.secretaryLine.setReadOnly(True)
        # self.iproLine.setReadOnly(True)
        #######

        self.frame_13 = QtWidgets.QFrame(self.frame_2)
        self.frame_13.setGeometry(QtCore.QRect(20, 340, 331, 61))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.financeminister = QtWidgets.QComboBox(self.frame_13)
        self.financeminister.setGeometry(QtCore.QRect(150, 10, 171, 41))
        self.financeminister.setObjectName("financeminister")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 141, 61))
        self.label_5.setObjectName("label_5")
        self.frame_15 = QtWidgets.QFrame(self.frame_2)
        self.frame_15.setGeometry(QtCore.QRect(370, 340, 331, 61))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.ipro = QtWidgets.QComboBox(self.frame_15)
        self.ipro.setGeometry(QtCore.QRect(150, 10, 171, 41))
        self.ipro.setObjectName("ipro")
        self.label_8 = QtWidgets.QLabel(self.frame_15)
        self.label_8.setGeometry(QtCore.QRect(80, 40, 141, 61))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 141, 61))
        self.label_9.setObjectName("label_9")
        self.vote = QtWidgets.QPushButton(self.centralwidget)
        self.vote.setGeometry(QtCore.QRect(740, 180, 111, 111))
        self.vote.setStyleSheet("color: blue;\n"
                                "font: bold;")
        self.vote.setObjectName("vote")
        ###
        self.vote.clicked.connect(self.voteCast)
        ###
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(750, 530, 89, 41))
        self.exit.setStyleSheet("color: blue;\n"
                                "font: bold;")
        self.exit.setObjectName("exit")
        ####
        self.exit.clicked.connect(self.exits)
        ####
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #########
        # The following are queries for the dropdown menus for the voters
        # If any change is altered in the registration the dropdowns also change
        #
        con = sqlite3.connect("E-VOTING.db")
        cur = con.cursor()
        result1 = cur.execute("SELECT NAME FROM candidates WHERE POSITION = 'PRESIDENT'")
        x1 = result1.fetchall()
        for check1 in x1:
            self.president.addItems(check1)

        result2 = cur.execute("SELECT NAME FROM candidates WHERE POSITION = 'VICE PRESIDENT'")
        x2 = result2.fetchall()
        for check2 in x2:
            self.vicepresident.addItems(check2)

        result3 = cur.execute("SELECT NAME FROM candidates WHERE POSITION = 'FINANCE MINISTER'")
        x3 = result3.fetchall()
        for check3 in x3:
            self.financeminister.addItems(check3)

        result4 = cur.execute("SELECT NAME FROM candidates WHERE POSITION = 'WELFARE MINISTER'")
        x4 = result4.fetchall()
        for check4 in x4:
            self.welfareminister.addItems(check4)

        result5 = cur.execute("SELECT NAME FROM candidates WHERE POSITION = 'SECRETARY GENERAL'")
        x5 = result5.fetchall()
        for check5 in x5:
            self.secretary.addItems(check5)

        result6 = cur.execute("SELECT NAME FROM candidates WHERE POSITION = 'IPRO'")
        x6 = result6.fetchall()
        for check6 in x6:
            self.ipro.addItems(check6)

        ########
        president = self.president.currentText()
        self.presidentLine.setText(president)

        vice = self.vicepresident.currentText()
        self.vicepresidentLine.setText(vice)

        finance = self.financeminister.currentText()
        self.financeministerLine.setText(finance)

        welfare = self.welfareminister.currentText()
        self.welfareministerLine.setText(welfare)

        secretary = self.secretary.currentText()
        self.secretaryLine.setText(secretary)

        ipro = self.ipro.currentText()
        self.iproLine.setText(ipro)
        ################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UTGSU E-VOTING SYSTEM"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#204a87;\">FULL NAME</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#204a87;\">MAT NUMBER</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">PRESIDENT</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#204a87;\">PRESIDENT</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">WELFARE MINISTER</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">VICE-PRESIDENT</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">SECRETARY</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">FINANCE MINISTER</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#204a87;\">PRESIDENT</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">IPRO</span></p></body></html>"))
        self.vote.setText(_translate("MainWindow", "VOTE"))
        self.exit.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Vote()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
