from PyQt5 import QtCore, QtGui, QtWidgets
#from adminsite import AdminSite

class StudentPopup(object):
    
    def popup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AdminSite()
        self.ui.setupUi(self.window)
        self.window.show()
        #MainWindow.hide()
    
    def ok(self):
        self.popup()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 243)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, 20, 531, 221))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 89, 25))
        self.pushButton.setStyleSheet("font: bold;\n"
"font-size: 20px;\n"
"color: blue;")
        self.pushButton.setObjectName("pushButton")
        
        ###################################################
        self.pushButton.clicked.connect(self.ok)
        ###################################################
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alert!!!!!"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#204a87;\">STUDENT </span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#204a87;\">REGISTERED</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#204a87;\">SUCCESSFULLY!!</span></p><p align=\"center\"><span style=\" font-size:28pt;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentPopup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
