# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\app\2048python\Help.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 150)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 250, 150))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Help"))
        self.textBrowser.setText(_translate("Form", "\n"
"    # 2048python #\n"
"\n"
"      ## version ##\n"
"\n"
"        2048python version 1.0\n"
"\n"
"        [2021/9/11]\n"
"\n"
"      ## rules ##\n"
"\n"
"        Each time you can choose to slide up and down in one direction, each time,all the digital blocks will be closeto the direction of sliding, the system will also appear in the blankspace of a number square, the samenumber of squares in close, collisionwill add up. The system gives the numbersquare is either 2 or 4, the player tofind a way in this small 16 grid rangeto come up with \"2048\" number square.\n"
"      "))
import Logo_rc
