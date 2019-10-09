# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow

from GUI.ventanaPrincipal import VentanaPrincipal

class Login1(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 380)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet\
            ("background-image: url(C:\Users\alexa\Pictures\Proyecto Grado\SoftwareHorarios\GUI\img\uq2.jpeg)")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 120, 261, 231))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtUsuario = QtWidgets.QTextEdit(self.frame)
        self.txtUsuario.setGeometry(QtCore.QRect(30, 40, 211, 31))
        self.txtUsuario.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border:1px solid gray;\n"                                     
"font: 75 10pt \"Century Gothic\";")
        self.txtUsuario.setObjectName("Usuario")
        self.txtUsuario.setPlaceholderText('Ingrese nombre de usuario')
        self.txtContrasena = QtWidgets.QTextEdit(self.frame)
        self.txtContrasena.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.txtContrasena.setStyleSheet("color: rgb(0, 51, 51);\n"
"background-color: rgb(189, 189, 189);\n"
"border:1px solid gray;\n"    
"font: 75 10pt \"Century Gothic\";\n"
"")
        self.txtContrasena.setObjectName("Contraseña")
        self.txtContrasena.setPlaceholderText('Ingrese contraseña')
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
        self.btnAgregar.clicked.connect(self.ingresar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ingresar(self):
        usuario = self.txtUsuario.toPlainText()
        contra = self.txtContrasena.toPlainText()
        if len(usuario) == 0 or len(contra) == 0:
            print("hola")
            self.mostrar_mensaje("Alerta", "¡Campos vacíos, verifique haber ingresado su usuario y contraseña!", "",
                                     QMessageBox.Warning, False)
            print("hola3")
        else:
            if usuario == 'admin' and contra == '12345':

             self.ventana = QtWidgets.QMainWindow()
             self.ui = VentanaPrincipal()
             print("6")
             self.ui.setup_ui(self.ventana)
             print("7")
             self.ventana.show()

            else:
             self.mostrar_mensaje("Alerta", "El usuario o la contraseña son incorrectos", "",
                                         QMessageBox.Warning,
                                         False)

    def mostrar_mensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox,
                            estado: bool):

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
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffff;\">Log-in</span></p></body></html>"))
        self.btnAgregar.setText(_translate("Form", "Iniciar Sesion"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Nombre de usuario:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Contraseña:</span></p></body></html>"))
