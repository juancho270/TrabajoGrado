# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 337)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textArchivo = QtWidgets.QTextEdit(Form)
        self.textArchivo.setEnabled(False)
        self.textArchivo.setGeometry(QtCore.QRect(120, 40, 471, 31))
        self.textArchivo.setObjectName("textArchivo")
        self.textTabla = QtWidgets.QTextEdit(Form)
        self.textTabla.setEnabled(False)
        self.textTabla.setGeometry(QtCore.QRect(120, 100, 471, 31))
        self.textTabla.setObjectName("textTabla")
        self.btnArchivo = QtWidgets.QPushButton(Form)
        self.btnArchivo.setGeometry(QtCore.QRect(600, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnArchivo.setFont(font)
        self.btnArchivo.setObjectName("btnArchivo")
        self.btnTabla = QtWidgets.QPushButton(Form)
        self.btnTabla.setGeometry(QtCore.QRect(600, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnTabla.setFont(font)
        self.btnTabla.setObjectName("btnTabla")
        self.btnSalir = QtWidgets.QPushButton(Form)
        self.btnSalir.setGeometry(QtCore.QRect(590, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(240, 160, 231, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btnCodificante = QtWidgets.QPushButton(self.groupBox)
        self.btnCodificante.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.btnCodificante.setObjectName("btnCodificante")
        self.btnNoCodificante = QtWidgets.QPushButton(self.groupBox)
        self.btnNoCodificante.setGeometry(QtCore.QRect(110, 30, 91, 31))
        self.btnNoCodificante.setObjectName("btnNoCodificante")
        self.btnNext = QtWidgets.QPushButton(Form)
        self.btnNext.setGeometry(QtCore.QRect(490, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNext.setFont(font)
        self.btnNext.setObjectName("btnNext")

        self.retranslateUi(Form)
        self.btnSalir.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ventana Principal"))
        self.label_2.setText(_translate("Form", "Ruta Archivo: "))
        self.label_3.setText(_translate("Form", "Ruta Tabla: "))
        self.btnArchivo.setText(_translate("Form", "Cargar"))
        self.btnTabla.setText(_translate("Form", "Cargar"))
        self.btnSalir.setText(_translate("Form", "Salir"))
        self.groupBox.setTitle(_translate("Form", "Generar Imagen"))
        self.btnCodificante.setText(_translate("Form", "Codificante"))
        self.btnNoCodificante.setText(_translate("Form", "No Codificante"))
        self.btnNext.setText(_translate("Form", "Siguiente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
