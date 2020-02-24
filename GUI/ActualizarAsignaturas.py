# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\ActualizarAsignaturas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ActualizarAsignatura(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 653)
        MainWindow.setStyleSheet("background-color: rgb(3, 169, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 341, 61))
        self.label_2.setStyleSheet("font: 75 8pt \"Century Gothic\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 60, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 90, 811, 521))
        self.frame.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.codigo_3 = QtWidgets.QLabel(self.frame)
        self.codigo_3.setGeometry(QtCore.QRect(40, 80, 211, 31))
        self.codigo_3.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.codigo_3.setObjectName("codigo_3")
        self.codigo_4 = QtWidgets.QLabel(self.frame)
        self.codigo_4.setGeometry(QtCore.QRect(90, 100, 101, 31))
        self.codigo_4.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.codigo_4.setObjectName("codigo_4")
        self.txtBuscarIdent = QtWidgets.QTextEdit(self.frame)
        self.txtBuscarIdent.setGeometry(QtCore.QRect(20, 140, 241, 31))
        self.txtBuscarIdent.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtBuscarIdent.setObjectName("txtBuscarIdent")
        self.btnBuscar = QtWidgets.QPushButton(self.frame)
        self.btnBuscar.setGeometry(QtCore.QRect(60, 230, 141, 31))
        self.btnBuscar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnBuscar.setObjectName("btnBuscar")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 40, 501, 461))
        self.groupBox_3.setStyleSheet("border: 1px solid gray;\n"
"font: 75 12pt \"Century Gothic\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.txtCodigo = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtCodigo.setGeometry(QtCore.QRect(240, 40, 241, 31))
        self.txtCodigo.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtCodigo.setObjectName("txtCodigo")
        self.txtNombre = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtNombre.setGeometry(QtCore.QRect(240, 90, 241, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtNombre.setObjectName("txtNombre")
        self.txtHorasSemestre = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtHorasSemestre.setGeometry(QtCore.QRect(240, 190, 241, 31))
        self.txtHorasSemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtHorasSemestre.setObjectName("txtHorasSemestre")
        self.txtRequsito = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtRequsito.setGeometry(QtCore.QRect(240, 240, 241, 31))
        self.txtRequsito.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtRequsito.setObjectName("txtRequsito")
        self.labeCodigo = QtWidgets.QLabel(self.groupBox_3)
        self.labeCodigo.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.labeCodigo.setStyleSheet("border: 0px solid gray;")
        self.labeCodigo.setObjectName("labeCodigo")
        self.labelNombre = QtWidgets.QLabel(self.groupBox_3)
        self.labelNombre.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.labelNombre.setStyleSheet("border: 0px solid gray;")
        self.labelNombre.setObjectName("labelNombre")
        self.labelNumeroCreditos = QtWidgets.QLabel(self.groupBox_3)
        self.labelNumeroCreditos.setGeometry(QtCore.QRect(20, 150, 161, 21))
        self.labelNumeroCreditos.setStyleSheet("border: 0px solid gray;")
        self.labelNumeroCreditos.setObjectName("labelNumeroCreditos")
        self.labelNumHoras = QtWidgets.QLabel(self.groupBox_3)
        self.labelNumHoras.setGeometry(QtCore.QRect(20, 200, 201, 21))
        self.labelNumHoras.setStyleSheet("border: 0px solid gray;")
        self.labelNumHoras.setObjectName("labelNumHoras")
        self.labelReq = QtWidgets.QLabel(self.groupBox_3)
        self.labelReq.setGeometry(QtCore.QRect(20, 250, 151, 21))
        self.labelReq.setStyleSheet("border: 0px solid gray;")
        self.labelReq.setObjectName("labelReq")
        self.labelSemestre = QtWidgets.QLabel(self.groupBox_3)
        self.labelSemestre.setGeometry(QtCore.QRect(20, 300, 101, 21))
        self.labelSemestre.setStyleSheet("border: 0px solid gray;")
        self.labelSemestre.setObjectName("labelSemestre")
        self.btnActualiza = QtWidgets.QPushButton(self.groupBox_3)
        self.btnActualiza.setGeometry(QtCore.QRect(300, 400, 141, 31))
        self.btnActualiza.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnActualiza.setObjectName("btnActualiza")
        self.btnLimpia = QtWidgets.QPushButton(self.groupBox_3)
        self.btnLimpia.setGeometry(QtCore.QRect(120, 400, 141, 31))
        self.btnLimpia.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnLimpia.setObjectName("btnLimpia")
        self.boxCreditos = QtWidgets.QSpinBox(self.groupBox_3)
        self.boxCreditos.setGeometry(QtCore.QRect(240, 140, 241, 31))
        self.boxCreditos.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.boxCreditos.setMinimum(1)
        self.boxCreditos.setMaximum(22)
        self.boxCreditos.setProperty("value", 1)
        self.boxCreditos.setObjectName("boxCreditos")
        self.boxSemestre = QtWidgets.QSpinBox(self.groupBox_3)
        self.boxSemestre.setGeometry(QtCore.QRect(240, 290, 241, 31))
        self.boxSemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.boxSemestre.setMinimum(1)
        self.boxSemestre.setMaximum(10)
        self.boxSemestre.setProperty("value", 1)
        self.boxSemestre.setObjectName("boxSemestre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 21))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Actualizar Asignatura</span></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo_3.setText(_translate("MainWindow", "<html><head/><body><p>Ingrese identificación de la</p><p><br/></p></body></html>"))
        self.codigo_4.setText(_translate("MainWindow", "<html><head/><body><p>asignatura</p><p><br/></p><p><br/></p></body></html>"))
        self.btnBuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Actualizar datos"))
        self.labeCodigo.setText(_translate("MainWindow", "Código:"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre:"))
        self.labelNumeroCreditos.setText(_translate("MainWindow", "Numero de creditos:"))
        self.labelNumHoras.setText(_translate("MainWindow", "Num. horas por semestre:"))
        self.labelReq.setText(_translate("MainWindow", "Cod. Requisito:"))
        self.labelSemestre.setText(_translate("MainWindow", "Semestre:"))
        self.btnActualiza.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.btnLimpia.setText(_translate("MainWindow", "LIMPIAR"))
