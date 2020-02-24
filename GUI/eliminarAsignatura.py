# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\eliminarAsignatura.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class EliminarAsignatura(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 328)
        MainWindow.setStyleSheet("background-color: rgb(3, 169, 244);\n"
"QTextEdit #txtNombre {\n"
"border-radius: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtCodtBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCodtBuscar.setGeometry(QtCore.QRect(180, 180, 201, 31))
        self.txtCodtBuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtCodtBuscar.setObjectName("txtCodtBuscar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 381, 61))
        self.label.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(300, 240, 91, 31))
        self.btnEliminar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(170, 240, 111, 31))
        self.btnLimpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.codigo_2 = QtWidgets.QLabel(self.centralwidget)
        self.codigo_2.setGeometry(QtCore.QRect(240, 150, 71, 21))
        self.codigo_2.setStyleSheet("font: 75 10pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")
        self.codigo_2.setObjectName("codigo_2")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(210, 130, 191, 21))
        self.codigo.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";")
        self.codigo.setObjectName("codigo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Eliminar asignaturas</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.btnEliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p>asignatura</p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p>Ingrese codigo de la</p><p><br/></p></body></html>"))
