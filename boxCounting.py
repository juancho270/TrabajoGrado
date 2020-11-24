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
        BoxCountig.resize(376, 310)
        self.btnCodificate = QtWidgets.QPushButton(BoxCountig)
        self.btnCodificate.setGeometry(QtCore.QRect(50, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCodificate.setFont(font)
        self.btnCodificate.setObjectName("btnCodificate")
        self.btnNoCodificante = QtWidgets.QPushButton(BoxCountig)
        self.btnNoCodificante.setGeometry(QtCore.QRect(210, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNoCodificante.setFont(font)
        self.btnNoCodificante.setObjectName("btnNoCodificante")
        self.btnAmbos = QtWidgets.QPushButton(BoxCountig)
        self.btnAmbos.setGeometry(QtCore.QRect(140, 250, 101, 31))
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
        self.label_5 = QtWidgets.QLabel(BoxCountig)
        self.label_5.setGeometry(QtCore.QRect(70, 120, 151, 16))
        self.label_5.setObjectName("label_5")
        self.DeltaCod = QtWidgets.QLabel(BoxCountig)
        self.DeltaCod.setGeometry(QtCore.QRect(220, 90, 101, 21))
        self.DeltaCod.setObjectName("DeltaCod")
        self.DeltaNoCod = QtWidgets.QLabel(BoxCountig)
        self.DeltaNoCod.setGeometry(QtCore.QRect(220, 119, 81, 21))
        self.DeltaNoCod.setObjectName("DeltaNoCod")
        self.DeltaCom = QtWidgets.QLabel(BoxCountig)
        self.DeltaCom.setGeometry(QtCore.QRect(220, 150, 91, 20))
        self.DeltaCom.setObjectName("DeltaCom")
        self.label_4 = QtWidgets.QLabel(BoxCountig)
        self.label_4.setGeometry(QtCore.QRect(70, 90, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(BoxCountig)
        self.label_7.setGeometry(QtCore.QRect(70, 150, 141, 16))
        self.label_7.setObjectName("label_7")

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
        self.label_5.setText(_translate("BoxCountig", "Delta Dq No Codificante:"))
        self.DeltaCod.setText(_translate("BoxCountig", "No Calculado"))
        self.DeltaNoCod.setText(_translate("BoxCountig", "No Calculado"))
        self.DeltaCom.setText(_translate("BoxCountig", "No Calculado"))
        self.label_4.setText(_translate("BoxCountig", "Delta Dq Codificante:"))
        self.label_7.setText(_translate("BoxCountig", "Delta Dq Completa:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BoxCountig = QtWidgets.QWidget()
    ui = Ui_BoxCountig()
    ui.setupUi(BoxCountig)
    BoxCountig.show()
    sys.exit(app.exec_())
