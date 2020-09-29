# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormImg(object):
    def setupUi(self, FormImg):
        FormImg.setObjectName("FormImg")
        FormImg.resize(699, 442)
        self.label_3 = QtWidgets.QLabel(FormImg)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormImg)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(FormImg)
        self.groupBox.setGeometry(QtCore.QRect(200, 350, 321, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btnBoxCounting = QtWidgets.QPushButton(self.groupBox)
        self.btnBoxCounting.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.btnBoxCounting.setObjectName("btnBoxCounting")
        self.btnDetrrended = QtWidgets.QPushButton(self.groupBox)
        self.btnDetrrended.setGeometry(QtCore.QRect(110, 30, 81, 31))
        self.btnDetrrended.setObjectName("btnDetrrended")
        self.btnDetrended2D = QtWidgets.QPushButton(self.groupBox)
        self.btnDetrended2D.setGeometry(QtCore.QRect(200, 30, 91, 31))
        self.btnDetrended2D.setObjectName("btnDetrended2D")
        self.labelImgCod = QtWidgets.QLabel(FormImg)
        self.labelImgCod.setGeometry(QtCore.QRect(30, 40, 301, 271))
        self.labelImgCod.setText("")
        self.labelImgCod.setObjectName("labelImgCod")
        self.labelImgNoCod = QtWidgets.QLabel(FormImg)
        self.labelImgNoCod.setGeometry(QtCore.QRect(360, 40, 301, 271))
        self.labelImgNoCod.setText("")
        self.labelImgNoCod.setObjectName("labelImgNoCod")

        self.retranslateUi(FormImg)
        QtCore.QMetaObject.connectSlotsByName(FormImg)

    def retranslateUi(self, FormImg):
        _translate = QtCore.QCoreApplication.translate
        FormImg.setWindowTitle(_translate("FormImg", "Imagenes"))
        self.label_3.setText(_translate("FormImg", "Codificante"))
        self.label_4.setText(_translate("FormImg", "No Codificante"))
        self.groupBox.setTitle(_translate("FormImg", "Seleccione Algoritmo"))
        self.btnBoxCounting.setText(_translate("FormImg", "Box Counting"))
        self.btnDetrrended.setText(_translate("FormImg", "Detrended"))
        self.btnDetrended2D.setText(_translate("FormImg", "Detrended 2D"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormImg = QtWidgets.QWidget()
    ui = Ui_FormImg()
    ui.setupUi(FormImg)
    FormImg.show()
    sys.exit(app.exec_())
