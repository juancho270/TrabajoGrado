# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boxCounting.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BoxCountig(object):
    def setupUi(self, BoxCountig):
        BoxCountig.setObjectName("BoxCountig")
        BoxCountig.resize(376, 205)
        self.btnCodificate = QtWidgets.QPushButton(BoxCountig)
        self.btnCodificate.setGeometry(QtCore.QRect(40, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCodificate.setFont(font)
        self.btnCodificate.setObjectName("btnCodificate")
        self.btnNoCodificante = QtWidgets.QPushButton(BoxCountig)
        self.btnNoCodificante.setGeometry(QtCore.QRect(200, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNoCodificante.setFont(font)
        self.btnNoCodificante.setObjectName("btnNoCodificante")
        self.btnAmbos = QtWidgets.QPushButton(BoxCountig)
        self.btnAmbos.setGeometry(QtCore.QRect(130, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAmbos.setFont(font)
        self.btnAmbos.setObjectName("btnAmbos")
        self.label_2 = QtWidgets.QLabel(BoxCountig)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.valorQ = QtWidgets.QComboBox(BoxCountig)
        self.valorQ.setGeometry(QtCore.QRect(130, 30, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.valorQ.setFont(font)
        self.valorQ.setObjectName("valorQ")
        self.valorQ.addItem("")
        self.valorQ.addItem("")
        self.valorQ.addItem("")
        self.valorQ.addItem("")
        self.valorQ.addItem("")
        self.valorQ.addItem("")

        self.retranslateUi(BoxCountig)
        QtCore.QMetaObject.connectSlotsByName(BoxCountig)

    def retranslateUi(self, BoxCountig):
        _translate = QtCore.QCoreApplication.translate
        BoxCountig.setWindowTitle(_translate("BoxCountig", "Box Counting"))
        self.btnCodificate.setText(_translate("BoxCountig", "Analisis Codificante"))
        self.btnNoCodificante.setText(_translate("BoxCountig", "Analisis No Codificante"))
        self.btnAmbos.setText(_translate("BoxCountig", "Ambas"))
        self.label_2.setText(_translate("BoxCountig", "Valor q:"))
        self.valorQ.setItemText(0, _translate("BoxCountig", "Seleccione una Opción"))
        self.valorQ.setItemText(1, _translate("BoxCountig", "-1 a 1"))
        self.valorQ.setItemText(2, _translate("BoxCountig", "-3 a 3"))
        self.valorQ.setItemText(3, _translate("BoxCountig", "-5 a 5"))
        self.valorQ.setItemText(4, _translate("BoxCountig", "-10 a 10"))
        self.valorQ.setItemText(5, _translate("BoxCountig", "-20 a 20"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BoxCountig = QtWidgets.QWidget()
    ui = Ui_BoxCountig()
    ui.setupUi(BoxCountig)
    BoxCountig.show()
    sys.exit(app.exec_())
