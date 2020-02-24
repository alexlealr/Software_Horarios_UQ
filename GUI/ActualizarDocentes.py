# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexa\Pictures\Proyecto Grado\Interfaces\ActualizarDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ActualizarDocente(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 645)
        MainWindow.setStyleSheet("background-color: rgb(3, 169, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, -10, 341, 61))
        self.label_2.setStyleSheet("font: 75 8pt \"Century Gothic\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 50, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 1221, 541))
        self.frame.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.codigo = QtWidgets.QLabel(self.frame)
        self.codigo.setGeometry(QtCore.QRect(40, 80, 201, 31))
        self.codigo.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.codigo.setObjectName("codigo")
        self.codigo_2 = QtWidgets.QLabel(self.frame)
        self.codigo_2.setGeometry(QtCore.QRect(90, 100, 101, 31))
        self.codigo_2.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.codigo_2.setObjectName("codigo_2")
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
        self.groupBox_3.setGeometry(QtCore.QRect(310, 20, 901, 491))
        self.groupBox_3.setStyleSheet("border: 1px solid gray;\n"
"font: 75 12pt \"Century Gothic\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.txtNombre = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtNombre.setGeometry(QtCore.QRect(210, 40, 241, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;\n"
"font: 10pt \"Century Gothic\";\n"
"border-radius: 5px;")
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtApellido.setGeometry(QtCore.QRect(210, 80, 241, 31))
        self.txtApellido.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtApellido.setObjectName("txtApellido")
        self.txtIdenti = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtIdenti.setGeometry(QtCore.QRect(210, 120, 241, 31))
        self.txtIdenti.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtIdenti.setObjectName("txtIdenti")
        self.txtGenero = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtGenero.setGeometry(QtCore.QRect(210, 160, 241, 31))
        self.txtGenero.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtGenero.setObjectName("txtGenero")
        self.txtResiden = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtResiden.setGeometry(QtCore.QRect(210, 200, 241, 31))
        self.txtResiden.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtResiden.setObjectName("txtResiden")
        self.textDirec = QtWidgets.QTextEdit(self.groupBox_3)
        self.textDirec.setGeometry(QtCore.QRect(210, 240, 241, 31))
        self.textDirec.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.textDirec.setObjectName("textDirec")
        self.txtPregr = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtPregr.setGeometry(QtCore.QRect(210, 280, 241, 31))
        self.txtPregr.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtPregr.setObjectName("txtPregr")
        self.txtPostgr = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtPostgr.setGeometry(QtCore.QRect(210, 320, 241, 31))
        self.txtPostgr.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtPostgr.setObjectName("txtPostgr")
        self.txtTelef = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtTelef.setGeometry(QtCore.QRect(210, 360, 241, 31))
        self.txtTelef.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtTelef.setObjectName("txtTelef")
        self.txtTrabInv = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtTrabInv.setGeometry(QtCore.QRect(210, 400, 241, 31))
        self.txtTrabInv.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Century Gothic\";\n"
"background-color: rgb(189, 189, 189);\n"
"border: 1px solid gray;")
        self.txtTrabInv.setObjectName("txtTrabInv")
        self.labelConcatena_2 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_2.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.labelConcatena_2.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_2.setObjectName("labelConcatena_2")
        self.labelConcatena_3 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_3.setGeometry(QtCore.QRect(20, 90, 111, 21))
        self.labelConcatena_3.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_3.setObjectName("labelConcatena_3")
        self.labelConcatena_4 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_4.setGeometry(QtCore.QRect(20, 130, 111, 21))
        self.labelConcatena_4.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_4.setObjectName("labelConcatena_4")
        self.labelConcatena_5 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_5.setGeometry(QtCore.QRect(20, 170, 111, 21))
        self.labelConcatena_5.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_5.setObjectName("labelConcatena_5")
        self.labelConcatena_6 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_6.setGeometry(QtCore.QRect(20, 210, 151, 21))
        self.labelConcatena_6.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_6.setObjectName("labelConcatena_6")
        self.labelConcatena_7 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_7.setGeometry(QtCore.QRect(20, 250, 101, 21))
        self.labelConcatena_7.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_7.setObjectName("labelConcatena_7")
        self.labelConcatena_8 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_8.setGeometry(QtCore.QRect(20, 290, 101, 21))
        self.labelConcatena_8.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_8.setObjectName("labelConcatena_8")
        self.labelConcatena_9 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_9.setGeometry(QtCore.QRect(20, 330, 101, 21))
        self.labelConcatena_9.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_9.setObjectName("labelConcatena_9")
        self.labelConcatena_10 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_10.setGeometry(QtCore.QRect(20, 370, 101, 21))
        self.labelConcatena_10.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_10.setObjectName("labelConcatena_10")
        self.labelConcatena_11 = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena_11.setGeometry(QtCore.QRect(20, 400, 151, 21))
        self.labelConcatena_11.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena_11.setObjectName("labelConcatena_11")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(480, 40, 311, 21))
        self.label_4.setStyleSheet("border: 0px solid gray;")
        self.label_4.setObjectName("label_4")
        self.comboAsignaturas = QtWidgets.QComboBox(self.groupBox_3)
        self.comboAsignaturas.setGeometry(QtCore.QRect(480, 80, 311, 31))
        self.comboAsignaturas.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 8pt \"Century Gothic\";")
        self.comboAsignaturas.setObjectName("comboAsignaturas")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(480, 140, 241, 21))
        self.label_3.setStyleSheet("border: 0px solid gray;")
        self.label_3.setObjectName("label_3")
        self.labelConcatena = QtWidgets.QLabel(self.groupBox_3)
        self.labelConcatena.setGeometry(QtCore.QRect(480, 170, 241, 21))
        self.labelConcatena.setStyleSheet("border: 0px solid gray;")
        self.labelConcatena.setObjectName("labelConcatena")
        self.btnElegir = QtWidgets.QPushButton(self.groupBox_3)
        self.btnElegir.setGeometry(QtCore.QRect(800, 80, 71, 31))
        self.btnElegir.setStyleSheet("font: 75 12pt \"Century Gothic\";\n"
"background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btnElegir.setObjectName("btnElegir")
        self.btnActualizar = QtWidgets.QPushButton(self.groupBox_3)
        self.btnActualizar.setGeometry(QtCore.QRect(670, 440, 141, 31))
        self.btnActualizar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnLimpiar = QtWidgets.QPushButton(self.groupBox_3)
        self.btnLimpiar.setGeometry(QtCore.QRect(490, 440, 141, 31))
        self.btnLimpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);\n"
"font:75 12pt \"Century Gothic\";")
        self.btnLimpiar.setObjectName("btnLimpiar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 21))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Actualizar Docente</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p>Ingrese identificación del</p><p/><p><br/></p></body></html>"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p>docente</p><p><br/></p></body></html>"))
        self.btnBuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Actualizar datos"))
        self.labelConcatena_2.setText(_translate("MainWindow", "Nombres:"))
        self.labelConcatena_3.setText(_translate("MainWindow", "Apellidos:"))
        self.labelConcatena_4.setText(_translate("MainWindow", "Identificación:"))
        self.labelConcatena_5.setText(_translate("MainWindow", "Genero:"))
        self.labelConcatena_6.setText(_translate("MainWindow", "Lugar de residencia:"))
        self.labelConcatena_7.setText(_translate("MainWindow", "Dirección:"))
        self.labelConcatena_8.setText(_translate("MainWindow", "Pregrado:"))
        self.labelConcatena_9.setText(_translate("MainWindow", "Postgrados:"))
        self.labelConcatena_10.setText(_translate("MainWindow", "Telefonos:"))
        self.labelConcatena_11.setText(_translate("MainWindow", "Trabajos de investi:"))
        self.label_4.setText(_translate("MainWindow", "Seleccione  las asignaturas del docente:"))
        self.label_3.setText(_translate("MainWindow", "Asignaturas seleccionadas:"))
        self.labelConcatena.setText(_translate("MainWindow", "Asignatura 1"))
        self.btnElegir.setText(_translate("MainWindow", "ELEGIR"))
        self.btnActualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
