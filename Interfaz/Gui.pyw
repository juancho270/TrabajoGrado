import sys
from Gui import *
from PyQt5.QtWidgets import *
from archivo import *


class Ventana(QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        """ self.ui.btnArchivo.clicked.connect(archivo.recuperar()) """


if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = Ventana()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
