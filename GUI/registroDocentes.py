# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\registroDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow

class  RegistroDocentes(QMainWindow):

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("Registro de docentes")
        MainWindow.resize(1010, 668)
        MainWindow.setStyleSheet("background-color: rgb(3, 169, 244);\n"
"QTextEdit #txtNombre {\n"
"border-radius: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 0, 341, 61))
        self.label.setStyleSheet("font: 75 8pt \"Century Gothic\";\n"
"")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 50, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(790, 500, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.asignatura_11 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_11.setGeometry(QtCore.QRect(70, 550, 131, 31))
        self.asignatura_11.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.asignatura_11.setObjectName("asignatura_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 90, 941, 531))
        self.frame.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtResiden = QtWidgets.QTextEdit(self.frame)
        self.txtResiden.setGeometry(QtCore.QRect(230, 200, 241, 31))
        self.txtResiden.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtResiden.setObjectName("txtResiden")
        self.txtApellido = QtWidgets.QTextEdit(self.frame)
        self.txtApellido.setGeometry(QtCore.QRect(230, 70, 241, 31))
        self.txtApellido.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtApellido.setObjectName("txtApellido")
        self.asignatura_3 = QtWidgets.QLabel(self.frame)
        self.asignatura_3.setGeometry(QtCore.QRect(40, 200, 171, 31))
        self.asignatura_3.setStyleSheet("\n"
"font: 75 8pt \"Century Gothic\";")
        self.asignatura_3.setObjectName("asignatura_3")
        self.identifi = QtWidgets.QLabel(self.frame)
        self.identifi.setGeometry(QtCore.QRect(40, 80, 141, 31))
        self.identifi.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.identifi.setObjectName("identifi")
        self.nombre = QtWidgets.QLabel(self.frame)
        self.nombre.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.nombre.setObjectName("nombre")
        self.txtIdenti = QtWidgets.QTextEdit(self.frame)
        self.txtIdenti.setGeometry(QtCore.QRect(230, 110, 241, 31))
        self.txtIdenti.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtIdenti.setObjectName("txtIdenti")
        self.asignatura_6 = QtWidgets.QLabel(self.frame)
        self.asignatura_6.setGeometry(QtCore.QRect(40, 320, 131, 31))
        self.asignatura_6.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.asignatura_6.setObjectName("asignatura_6")
        self.asignatura_8 = QtWidgets.QLabel(self.frame)
        self.asignatura_8.setGeometry(QtCore.QRect(40, 400, 181, 31))
        self.asignatura_8.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.asignatura_8.setObjectName("asignatura_8")
        self.asignatura_4 = QtWidgets.QLabel(self.frame)
        self.asignatura_4.setGeometry(QtCore.QRect(40, 280, 131, 31))
        self.asignatura_4.setStyleSheet("\n"
"font: 75 8pt \"Century Gothic\";")
        self.asignatura_4.setObjectName("asignatura_4")
        self.txtGenero = QtWidgets.QTextEdit(self.frame)
        self.txtGenero.setGeometry(QtCore.QRect(230, 150, 241, 31))
        self.txtGenero.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtGenero.setObjectName("txtGenero")
        self.txtPregr = QtWidgets.QTextEdit(self.frame)
        self.txtPregr.setGeometry(QtCore.QRect(230, 280, 241, 31))
        self.txtPregr.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtPregr.setObjectName("txtPregr")
        self.txtTelef = QtWidgets.QTextEdit(self.frame)
        self.txtTelef.setGeometry(QtCore.QRect(230, 360, 241, 31))
        self.txtTelef.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtTelef.setObjectName("txtTelef")
        self.asignatura_7 = QtWidgets.QLabel(self.frame)
        self.asignatura_7.setGeometry(QtCore.QRect(40, 360, 131, 31))
        self.asignatura_7.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.asignatura_7.setObjectName("asignatura_7")
        self.textDirec = QtWidgets.QTextEdit(self.frame)
        self.textDirec.setGeometry(QtCore.QRect(230, 240, 241, 31))
        self.textDirec.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.textDirec.setObjectName("textDirec")
        self.tipo = QtWidgets.QLabel(self.frame)
        self.tipo.setGeometry(QtCore.QRect(40, 110, 111, 31))
        self.tipo.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.tipo.setObjectName("tipo")
        self.asignatura_2 = QtWidgets.QLabel(self.frame)
        self.asignatura_2.setGeometry(QtCore.QRect(40, 160, 141, 31))
        self.asignatura_2.setStyleSheet("\n"
"font: 75 8pt \"Century Gothic\";")
        self.asignatura_2.setObjectName("asignatura_2")
        self.txtTrabInv = QtWidgets.QTextEdit(self.frame)
        self.txtTrabInv.setGeometry(QtCore.QRect(230, 400, 241, 31))
        self.txtTrabInv.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtTrabInv.setObjectName("txtTrabInv")
        self.asignatura_5 = QtWidgets.QLabel(self.frame)
        self.asignatura_5.setGeometry(QtCore.QRect(40, 240, 131, 31))
        self.asignatura_5.setStyleSheet("font: 75 8pt \"Century Gothic\";")
        self.asignatura_5.setObjectName("asignatura_5")
        self.txtNombre = QtWidgets.QTextEdit(self.frame)
        self.txtNombre.setGeometry(QtCore.QRect(230, 30, 241, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtNombre.setObjectName("txtNombre")
        self.txtPostgr = QtWidgets.QTextEdit(self.frame)
        self.txtPostgr.setGeometry(QtCore.QRect(230, 320, 241, 31))
        self.txtPostgr.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtPostgr.setObjectName("txtPostgr")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(490, 30, 431, 401))
        self.groupBox.setStyleSheet("border: 1px solid gray;\n"
"font: 75 12pt \"Century Gothic\";")
        self.groupBox.setObjectName("groupBox")
        self.comboAsignaturas = QtWidgets.QComboBox(self.groupBox)
        self.comboAsignaturas.setGeometry(QtCore.QRect(10, 80, 311, 31))
        self.comboAsignaturas.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 8pt \"Century Gothic\";")
        self.comboAsignaturas.setObjectName("comboAsignaturas")
        self.btnElegir = QtWidgets.QPushButton(self.groupBox)
        self.btnElegir.setGeometry(QtCore.QRect(340, 80, 71, 31))
        self.btnElegir.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btnElegir.setObjectName("btnElegir")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 241, 21))
        self.label_2.setStyleSheet("border: 0px solid gray;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 311, 21))
        self.label_3.setStyleSheet("border: 0px solid gray;")
        self.label_3.setObjectName("label_3")
        self.labelConcatena = QtWidgets.QLabel(self.groupBox)
        self.labelConcatena.setGeometry(QtCore.QRect(10, 170, 241, 21))
        self.labelConcatena.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena.setObjectName("labelConcatena")
        self.btnLimpiar = QtWidgets.QPushButton(self.frame)
        self.btnLimpiar.setGeometry(QtCore.QRect(310, 470, 141, 31))
        self.btnLimpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnRegistrar = QtWidgets.QPushButton(self.frame)
        self.btnRegistrar.setGeometry(QtCore.QRect(490, 470, 141, 31))
        self.btnRegistrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnRegistrar.setObjectName("btnRegistrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnRegistrar.clicked.connect(self.btnRegistrar.showMenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Registro de Docentes</span></p></body></html>"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.asignatura_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Asignaturas:</span></p></body></html>"))
        self.asignatura_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Lugar de residencia:</span></p></body></html>"))
        self.identifi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Apellidos:</span></p><p><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Nombres:</span></p><p><br/></p></body></html>"))
        self.asignatura_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Postgrados:</span></p></body></html>"))
        self.asignatura_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Trabajos de investi</span><span style=\" font-size:12pt; color:#ffffff;\">.:</span></p><p><br/></p></body></html>"))
        self.asignatura_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Pregrado:</span></p></body></html>"))
        self.asignatura_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Telefonos:</span></p></body></html>"))
        self.tipo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Identificación:</span></p></body></html>"))
        self.asignatura_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Genero:</span></p><p><br/></p></body></html>"))
        self.asignatura_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Dirección:</span></p><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Asignaturas del docente"))
        self.btnElegir.setText(_translate("MainWindow", "ELEGIR"))
        self.label_2.setText(_translate("MainWindow", "Asignaturas seleccionadas:"))
        self.label_3.setText(_translate("MainWindow", "Seleccione  las asignaturas del docente:"))
        self.labelConcatena.setText(_translate("MainWindow", "Asignatura 1"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnRegistrar.setText(_translate("MainWindow", "REGISTRAR"))
