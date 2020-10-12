import sys
from detrended import *
from Algoritmos.detrended import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from archivo import archivo
from archivo import *
import numpy as np


class ventanaDetrended(QWidget):
    def __init__(self, parent, nombre):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_detrend()
        self.ui.setupUi(self)
        self.ui.btnCodificanteA.clicked.connect(
            self.analisisCodificante)
        self.ui.btnNoCodificanteA.clicked.connect(
            self.analisisCodificante)
        self.nombreArchivo = nombre
        # self.resize(pixmapNoCod.width(),pixmapNoCod.height())

    def imprimir(self):
        print('metodo')

    def analisisCodificante(self):
        rangoQ = np.zeros(1)
        escalaSeleccionada = 0
        distancia = 0.0
        if self.ui.valorQ.currentText() != 'Seleccione una Opcion' and self.ui.escalas.currentText() != 'Seleccione una Opcion' and self.ui.distancia.toPlainText() != '':
            escalaSeleccionada = int(self.ui.escalas.currentText())
            try:
                distancia = float(self.ui.distancia.toPlainText())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Faltan Selecciones")
                msg.setInformativeText(
                    "La distancia q debe ser decimal")
                msg.setWindowTitle("Error")
                retval = msg.exec_()
            if self.ui.valorQ.currentText() == '-1 a 1':
                rango1 = np.arange(-1.0, -0.2, distancia)
                rango2 = np.arange(0.2, 1.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rango1 = np.arange(-3.0, -0.2, distancia)
                rango2 = np.arange(0.2, 3.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rango1 = np.arange(-5.0, -0.2, distancia)
                rango2 = np.arange(0.2, 5.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rango1 = np.arange(-10.0, -0.2, distancia)
                rango2 = np.arange(0.2, 10.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rango1 = np.arange(-20.0, -0.2, distancia)
                rango2 = np.arange(0.2, 20.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            data = detrended.lineaTiempo("ArchivosGenerados/Secuencias/Codificante/" +
                                         self.nombreArchivo + "_codificante.fasta")
            time = detrended.transformada(data)
            lag = detrended.divisiones(time, escalaSeleccionada)
            resultados = np.zeros(rangoQ.size)
            for i in range(0, rangoQ.size):
                hurst = detrended.detrendedAnality(
                    time, lag, rangoQ[i], int(self.ui.lblGrado.text()), "ArchivosGenerados/Resultados/Codificante/" +
                    self.nombreArchivo + "_codificante.fasta")
                resultados[i] = hurst
            plt.plot(rangoQ, resultados, 'b')
            plt.show()
            print(rangoQ, resultados)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()


if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = ventanaDetrended()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
