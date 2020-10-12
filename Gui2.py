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
        FormImg.resize(849, 463)
        self.label_3 = QtWidgets.QLabel(FormImg)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormImg)
        self.label_4.setGeometry(QtCore.QRect(570, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labelImgCod = QtWidgets.QLabel(FormImg)
        self.labelImgCod.setGeometry(QtCore.QRect(60, 40, 341, 271))
        self.labelImgCod.setText("")
        self.labelImgCod.setObjectName("labelImgCod")
        self.labelImgNoCod = QtWidgets.QLabel(FormImg)
        self.labelImgNoCod.setGeometry(QtCore.QRect(460, 40, 341, 271))
        self.labelImgNoCod.setText("")
        self.labelImgNoCod.setObjectName("labelImgNoCod")
        self.groupBox_2 = QtWidgets.QGroupBox(FormImg)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 320, 381, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnBoxCounting = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBoxCounting.setGeometry(QtCore.QRect(270, 50, 91, 31))
        self.btnBoxCounting.setObjectName("btnBoxCounting")
        self.btnDetrended2D = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDetrended2D.setGeometry(QtCore.QRect(140, 50, 91, 31))
        self.btnDetrended2D.setObjectName("btnDetrended2D")
        self.btnDetrrended = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDetrrended.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.btnDetrrended.setObjectName("btnDetrrended")

        self.retranslateUi(FormImg)
        QtCore.QMetaObject.connectSlotsByName(FormImg)

    def retranslateUi(self, FormImg):
        _translate = QtCore.QCoreApplication.translate
        FormImg.setWindowTitle(_translate("FormImg", "Imagenes"))
        self.label_3.setText(_translate("FormImg", "Codificante"))
        self.label_4.setText(_translate("FormImg", "No Codificante"))
        self.groupBox_2.setTitle(_translate("FormImg", "Seleccione metodo"))
        self.btnBoxCounting.setText(_translate("FormImg", "Box Counting"))
        self.btnDetrended2D.setText(_translate("FormImg", "Detrended 2D"))
        self.btnDetrrended.setText(_translate("FormImg", "Detrended"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormImg = QtWidgets.QWidget()
    ui = Ui_FormImg()
    ui.setupUi(FormImg)
    FormImg.show()
    sys.exit(app.exec_())
