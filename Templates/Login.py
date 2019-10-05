# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow

class Login(QMainWindow):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 380)
        Form.setStyleSheet("background-color: rgb(3, 169, 244);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 120, 261, 231))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 211, 31))
        self.textEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"font: 75 11pt \"Century Gothic\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.textEdit_2.setStyleSheet("color: rgb(0, 51, 51);\n"
"background-color: rgb(189, 189, 189);\n"
"font: 75 11pt \"Century Gothic\";\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.btnAgregar = QtWidgets.QPushButton(self.frame)
        self.btnAgregar.setGeometry(QtCore.QRect(30, 170, 211, 41))
        self.btnAgregar.setStyleSheet("font:75 14pt \"Century Gothic\";\n"
"color: rgb(255, 255,255);\n"
"background-color: rgb(117, 117, 117);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 141, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"Century Gothic\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 91, 20))
        self.label_3.setStyleSheet("font: 75 10pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffff;\">Log-in</span></p></body></html>"))
        self.btnAgregar.setText(_translate("Form", "Iniciar Sesion"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Nombre de usuario:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Contraseña:</span></p></body></html>"))
