import sys
from Gui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from archivo import archivo
from archivo import *


class Ventana(QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnArchivo.clicked.connect(self.cargaArchivo)
        self.ui.btnTabla.clicked.connect(self.tabla)
        self.ui.btnCodificante.clicked.connect(self.codificante)
        self.ui.btnNoCodificante.clicked.connect(self.noCodificante)
        self.carga = False
        self.cargaTabla = False

    def tabla(self):
        ruta = archivo.recuperarTabla(self)
        self.ui.textTabla.setPlainText(ruta)
        self.cargaTabla = True

    def cargaArchivo(self):
        ruta = archivo.recuperar(self)
        self.ui.textArchivo.setPlainText(ruta)
        self.carga = True

    def codificante(self):
        if self.carga and self.cargaTabla:
            kmers = self.ui.NoKmers.text()
            archivo.hacerImagenCodificante(int(kmers))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("No se han cargado archivos")
            msg.setInformativeText(
                "Se deben cargar los archivos con la secuencia y la informacion")
            msg.setWindowTitle("Error")
            retval = msg.exec_()
            print("value of pressed message box button:", retval)

    def noCodificante(self):
        if self.carga and self.cargaTabla:
            kmers = self.ui.NoKmers.text()
            archivo.hacerImagenNoCodificante(int(kmers))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("No se han cargado archivos")
            msg.setInformativeText(
                "Se deben cargar los archivos con la secuencia y la informacion")
            msg.setWindowTitle("Error")
            retval = msg.exec_()
            print("value of pressed message box button:", retval)


if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = Ventana()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
