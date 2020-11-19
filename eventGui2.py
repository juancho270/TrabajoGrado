import sys
from Gui2 import *
from detrendedLogic import *
from detrend2DLogic import *
from boxCountingLogic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from archivo import archivo
from archivo import *


class Ventana2(QWidget):
    def __init__(self, parent, nombre):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormImg()
        self.ui.setupUi(self)
        self.ui.btnBoxCounting.clicked.connect(self.openVentanaBoxCounting)
        self.ui.btnDetrended2D.clicked.connect(self.openVentanaDetrended2D)
        self.pixmapCod = QPixmap(
            "Imagenes/Codificante/" + nombre + "_codificante.jpg")
        self.pixmapNoCod = QPixmap(
            "Imagenes/NoCodificante/" + nombre + "_noCodificante.jpg")
        self.pixmapCod2 = self.pixmapCod.scaled(self.ui.labelImgCod.width(),
                                                self.ui.labelImgCod.height())
        self.pixmapNoCod2 = self.pixmapNoCod.scaled(
            self.ui.labelImgNoCod.width(), self.ui.labelImgNoCod.height())
        self.ui.labelImgCod.setPixmap(self.pixmapCod2)
        self.ui.labelImgNoCod.setPixmap(self.pixmapNoCod2)
        self.ui.btnDetrrended.clicked.connect(self.openVentanaDetrended)
        self.nombreArchivo = nombre

        # self.resize(pixmapNoCod.width(),pixmapNoCod.height())

    def openVentanaDetrended(self):
        self.ventana = ventanaDetrended(None, self.nombreArchivo)
        self.ventana.show()

    def openVentanaBoxCounting(self):
        self.ventana = ventanaBoxCounting(None, self.nombreArchivo)
        self.ventana.show()

    def openVentanaDetrended2D(self):
        self.ventana = ventanaDetrended2D(None, self.nombreArchivo)
        self.ventana.show()


if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = Ventana2()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
