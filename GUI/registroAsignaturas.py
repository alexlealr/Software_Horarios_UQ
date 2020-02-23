# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\registroAsignaturas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 575)
        MainWindow.setStyleSheet("background-color: rgb(3, 169, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, -10, 371, 61))
        self.label.setStyleSheet("font: 75 8pt \"Century Gothic\";\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 90, 531, 441))
        self.frame.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtRequisito = QtWidgets.QTextEdit(self.frame)
        self.txtRequisito.setGeometry(QtCore.QRect(250, 230, 241, 31))
        self.txtRequisito.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtRequisito.setObjectName("txtRequisito")
        self.txtNombre = QtWidgets.QTextEdit(self.frame)
        self.txtNombre.setGeometry(QtCore.QRect(250, 80, 241, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtNombre.setObjectName("txtNombre")
        self.horasSemestres = QtWidgets.QLabel(self.frame)
        self.horasSemestres.setGeometry(QtCore.QRect(40, 190, 201, 31))
        self.horasSemestres.setStyleSheet("\n"
"font: 75 8pt \"Century Gothic\";")
        self.horasSemestres.setObjectName("horasSemestres")
        self.codigo = QtWidgets.QLabel(self.frame)
        self.codigo.setGeometry(QtCore.QRect(40, 40, 141, 31))
        self.codigo.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.codigo.setObjectName("codigo")
        self.semestre = QtWidgets.QLabel(self.frame)
        self.semestre.setGeometry(QtCore.QRect(40, 280, 131, 31))
        self.semestre.setStyleSheet("\n"
"font: 75 8pt \"Century Gothic\";")
        self.semestre.setObjectName("semestre")
        self.txtHorasSemestre = QtWidgets.QTextEdit(self.frame)
        self.txtHorasSemestre.setGeometry(QtCore.QRect(250, 180, 241, 31))
        self.txtHorasSemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtHorasSemestre.setObjectName("txtHorasSemestre")
        self.nombre = QtWidgets.QLabel(self.frame)
        self.nombre.setGeometry(QtCore.QRect(40, 90, 111, 31))
        self.nombre.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.nombre.setObjectName("nombre")
        self.creditos = QtWidgets.QLabel(self.frame)
        self.creditos.setGeometry(QtCore.QRect(40, 140, 171, 31))
        self.creditos.setStyleSheet("\n"
"font: 75 8pt \"Century Gothic\";")
        self.creditos.setObjectName("creditos")
        self.codRequisito = QtWidgets.QLabel(self.frame)
        self.codRequisito.setGeometry(QtCore.QRect(40, 240, 131, 31))
        self.codRequisito.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.codRequisito.setObjectName("codRequisito")
        self.txtCodigo = QtWidgets.QTextEdit(self.frame)
        self.txtCodigo.setGeometry(QtCore.QRect(250, 30, 241, 31))
        self.txtCodigo.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtCodigo.setObjectName("txtCodigo")
        self.btnLimpia = QtWidgets.QPushButton(self.frame)
        self.btnLimpia.setGeometry(QtCore.QRect(130, 370, 141, 31))
        self.btnLimpia.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnLimpia.setObjectName("btnLimpia")
        self.btnRegistrar = QtWidgets.QPushButton(self.frame)
        self.btnRegistrar.setGeometry(QtCore.QRect(300, 370, 141, 31))
        self.btnRegistrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.boxCreditos = QtWidgets.QSpinBox(self.frame)
        self.boxCreditos.setGeometry(QtCore.QRect(250, 130, 241, 31))
        self.boxCreditos.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.boxCreditos.setMinimum(1)
        self.boxCreditos.setMaximum(22)
        self.boxCreditos.setProperty("value", 1)
        self.boxCreditos.setObjectName("boxCreditos")
        self.boxSemestre = QtWidgets.QSpinBox(self.frame)
        self.boxSemestre.setGeometry(QtCore.QRect(250, 280, 241, 31))
        self.boxSemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.boxSemestre.setMinimum(1)
        self.boxSemestre.setMaximum(10)
        self.boxSemestre.setProperty("value", 1)
        self.boxSemestre.setObjectName("boxSemestre")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(190, 60, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Registro de Asignaturas</span></p></body></html>"))
        self.horasSemestres.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Num. horas por semestre:</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Codigo:</span></p><p><br/></p></body></html>"))
        self.semestre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Semestre:</span></p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Nombre:</span></p></body></html>"))
        self.creditos.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Numero de creditos:</span></p><p><br/></p></body></html>"))
        self.codRequisito.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Cod. Requisito:</span></p><p><br/></p></body></html>"))
        self.btnLimpia.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnRegistrar.setText(_translate("MainWindow", "REGISTRAR"))
