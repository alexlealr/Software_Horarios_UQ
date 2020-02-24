# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\eliminarDocente.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class EliminarDocente(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 321)
        MainWindow.setStyleSheet("background-color: rgb(3, 169, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 381, 61))
        self.label.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.txtIdentBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIdentBuscar.setGeometry(QtCore.QRect(170, 180, 201, 31))
        self.txtIdentBuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtIdentBuscar.setObjectName("txtIdentBuscar")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(190, 120, 191, 31))
        self.codigo.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";")
        self.codigo.setObjectName("codigo")
        self.codigo_2 = QtWidgets.QLabel(self.centralwidget)
        self.codigo_2.setGeometry(QtCore.QRect(250, 140, 61, 21))
        self.codigo_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";")
        self.codigo_2.setObjectName("codigo_2")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(160, 230, 111, 31))
        self.btnLimpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(290, 230, 91, 31))
        self.btnEliminar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.btnEliminar.setObjectName("btnEliminar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Eliminar docentes</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p>Ingrese identificación del</p><p/><p><br/></p></body></html>"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p>docente</p><p><br/></p></body></html>"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnEliminar.setText(_translate("MainWindow", "ELIMINAR"))
