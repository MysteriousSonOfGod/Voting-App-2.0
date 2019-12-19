from PyQt5 import QtCore, QtGui, QtWidgets

class Voted(object):
    
    def exitButton(self):
        exit()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, -20, 531, 221))
        self.label.setObjectName("label")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(130, 170, 111, 31))
        self.exit.setStyleSheet("font: bold;\n"
"font-size: blue;\n"
"color: blue;")
        self.exit.setObjectName("exit")
        ##########################################
        self.exit.clicked.connect(self.exitButton)
        ##########################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alert!!!"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#204a87;\">VOTED</span></p></body></html>"))
        self.exit.setText(_translate("MainWindow", "EXIT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Voted()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
