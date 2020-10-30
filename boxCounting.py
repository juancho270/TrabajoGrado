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
        BoxCountig.resize(299, 176)
        self.label = QtWidgets.QLabel(BoxCountig)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBoxN = QtWidgets.QComboBox(BoxCountig)
        self.comboBoxN.setGeometry(QtCore.QRect(110, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxN.setFont(font)
        self.comboBoxN.setObjectName("comboBoxN")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.comboBoxN.addItem("")
        self.btnCodificate = QtWidgets.QPushButton(BoxCountig)
        self.btnCodificate.setGeometry(QtCore.QRect(30, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCodificate.setFont(font)
        self.btnCodificate.setObjectName("btnCodificate")
        self.btnNoCodificante = QtWidgets.QPushButton(BoxCountig)
        self.btnNoCodificante.setGeometry(QtCore.QRect(150, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNoCodificante.setFont(font)
        self.btnNoCodificante.setObjectName("btnNoCodificante")

        self.retranslateUi(BoxCountig)
        QtCore.QMetaObject.connectSlotsByName(BoxCountig)

    def retranslateUi(self, BoxCountig):
        _translate = QtCore.QCoreApplication.translate
        BoxCountig.setWindowTitle(_translate("BoxCountig", "Box Counting"))
        self.label.setText(_translate("BoxCountig", "Valor de N:"))
        self.comboBoxN.setItemText(0, _translate("BoxCountig", "Seleccione un Valor"))
        self.comboBoxN.setItemText(1, _translate("BoxCountig", "1"))
        self.comboBoxN.setItemText(2, _translate("BoxCountig", "2"))
        self.comboBoxN.setItemText(3, _translate("BoxCountig", "3"))
        self.comboBoxN.setItemText(4, _translate("BoxCountig", "4"))
        self.comboBoxN.setItemText(5, _translate("BoxCountig", "5"))
        self.comboBoxN.setItemText(6, _translate("BoxCountig", "6"))
        self.comboBoxN.setItemText(7, _translate("BoxCountig", "7"))
        self.comboBoxN.setItemText(8, _translate("BoxCountig", "8"))
        self.btnCodificate.setText(_translate("BoxCountig", "Codificante"))
        self.btnNoCodificante.setText(_translate("BoxCountig", "No Codificante"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BoxCountig = QtWidgets.QWidget()
    ui = Ui_BoxCountig()
    ui.setupUi(BoxCountig)
    BoxCountig.show()
    sys.exit(app.exec_())
