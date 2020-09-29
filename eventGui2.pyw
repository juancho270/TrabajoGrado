import sys
from Gui2 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from archivo import archivo
from archivo import *


class Ventana2(QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_FormImg()
        self.ui.setupUi(self)
        self.ui.btnBoxCounting.clicked.connect(self.imprimir)
        self.pixmapCod = QPixmap('Codificante.jpg')
        self.pixmapNoCod = QPixmap('noCodificante.jpg')
        self.pixmapCod2 = self.pixmapCod.scaled(self.ui.labelImgCod.width(),
                                                self.ui.labelImgCod.height())
        self.pixmapNoCod2 = self.pixmapNoCod.scaled(
            self.ui.labelImgNoCod.width(), self.ui.labelImgNoCod.height())
        self.ui.labelImgCod.setPixmap(self.pixmapCod2)
        self.ui.labelImgNoCod.setPixmap(self.pixmapNoCod2)

        # self.resize(pixmapNoCod.width(),pixmapNoCod.height())

    def imprimir(self):
        print('hola')


if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = Ventana2()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
