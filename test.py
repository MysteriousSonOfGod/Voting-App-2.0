

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_Form(object):
    def name(self):
        names = input("Enter your name ")
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(491, 320)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 90, 67, 17))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(110, 90, 281, 17))
        self.name.setObjectName(self.name)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "name:"))
        self.name.setText(_translate("Form", "name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
