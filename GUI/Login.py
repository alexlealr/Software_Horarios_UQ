# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.ventanaPrincipal import VentanaPrincipal
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication


class Login(object):

    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 598)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 40, 201, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, -10, 831, 611))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("/uq2.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(240, 220, 271, 271))
        self.label_6.setStyleSheet("background-color: rgb(0,0,0,50%);\n"
                                   "border-radius: 5px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 280, 141, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"Century Gothic\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.txtUsuario = QtWidgets.QTextEdit(Form)
        self.txtUsuario.setGeometry(QtCore.QRect(270, 310, 211, 31))
        self.txtUsuario.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "border-radius: 5px;\n"
                                      "background-color: rgb(189, 189, 189);\n"
                                      "font: 75 10pt \"Century Gothic\";")
        self.txtUsuario.setObjectName("Usuario")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 350, 91, 20))
        self.label_3.setStyleSheet("font: 75 10pt \"Century Gothic\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txtContra = QtWidgets.QTextEdit(Form)
        self.txtContra.setGeometry(QtCore.QRect(270, 380, 211, 31))
        self.txtContra.setStyleSheet("color: rgb(0, 51, 51);\n"
                                     "border-radius: 5px;\n"
                                     "background-color: rgb(189, 189, 189);\n"
                                     "font: 75 11pt \"Century Gothic\";\n"
                                     "")
        self.txtContra.setObjectName("Contraseña")
        self.btnAgregar = QtWidgets.QPushButton(Form)
        self.btnAgregar.setGeometry(QtCore.QRect(270, 430, 211, 41))
        self.btnAgregar.setStyleSheet("font:75 14pt \"Century Gothic\";\n"
                                      "background-color: rgb(25, 118, 210);\n"
                                      "color: rgb(255, 255, 255);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(240, 220, 271, 41))
        self.label_7.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                   "font: 75 16pt \"Century Gothic\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius: 5px;")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        self.btnAgregar.clicked.connect(self.ingresar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ingresar(self):
        usuario = self.txtUsuario.toPlainText()
        print(usuario)
        contra = self.txtContra.toPlainText()
        print("añex")
        if len(usuario) == 0 | len(contra) == 0:
            self.mostrarMensaje("Alerta", "Ingrese usuario y/o contraseña", "", QMessageBox.Warning, False)
        else:
            if usuario == 'admin' and contra == '12345':
                print('alex')
                self.ventana = QtWidgets.QMainWindow()
                print("aksas")
                self.ui = VentanaPrincipal()
                print("3232323")
                self.ui.setup_ui(self.ventana)
                self.ventana.show()
            else:
                self.mostrarMensaje("Alerta", "El usuario o la contraseña son incorrectos", "", QMessageBox.Warning,
                                    False)

    def mostrarMensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox, estado: bool):

        self.message_box = QMessageBox()
        self.message_box.setWindowTitle(titulo)
        self.message_box.setText(texto)

        if len(texto_informativo) > 0:
            self.message_box.setInformativeText(texto_informativo)

        if estado:
            btn_si = self.message_box.addButton('Si', QMessageBox.ActionRole)
            btn_no = self.message_box.addButton('No', QMessageBox.ActionRole)
            self.message_box.setDefaultButton(btn_si, btn_no)
        else:
            btn_aceptar = self.message_box.addButton('Aceptar', QMessageBox.ActionRole)
            self.message_box.setDefaultButton(btn_aceptar)
        if tipo_mensaje is not None:
            self.message_box.setIcon(tipo_mensaje)
            self.message_box.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p><img src=\":/uq2.jpeg\"/></p></body></html>"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Nombre de usuario:</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Contraseña:</span></p></body></html>"))
        self.btnAgregar.setText(_translate("Form", "Iniciar Sesion"))
        self.label_7.setText(_translate("Form", "                Log-in"))
