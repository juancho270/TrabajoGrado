import sys
from boxCounting import *
from Algoritmos.boxCounting import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from archivo import archivo
from archivo import *
import numpy as np
import imageio


class ventanaBoxCounting(QWidget):
    def __init__(self, parent, nombre):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_BoxCountig()
        self.ui.setupUi(self)
        self.ui.btnCodificate.clicked.connect(self.btnCodificanteAction)
        self.ui.btnNoCodificante.clicked.connect(self.btnNoCodificanteAction)
        self.nombreArchivo = nombre

    def btnCodificanteAction(self):
        I = boxCounting.rgb2gray(imageio.imread(
            "Imagenes/Codificante/" + self.nombreArchivo + "_codificante.jpg"))
        print("Minkowski–Bouligand dimension (computed): ",
              boxCounting.fractal_dimension(I, self.nombreArchivo + "Codificante", 'Codificante'))

    def btnNoCodificanteAction(self):
        n = self.ui.comboBoxN.currentText() + self.nombreArchivo
        I = boxCounting.rgb2gray(imageio.imread(
            "Imagenes/NoCodificante/" + self.nombreArchivo + "_noCodificante.jpg"))
        print("Minkowski–Bouligand dimension (computed): ",
              boxCounting.fractal_dimension(I, self.nombreArchivo + "_noCodificante", 'NoCodificante'))


if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = ventanaBoxCounting()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
