import sys
from boxCounting import *
from Algoritmos.boxCounting import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from archivo import archivo
from archivo import *
import numpy as np
import imageio
import pylab as pl


class ventanaBoxCounting(QWidget):
    def __init__(self, parent, nombre):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_BoxCountig()
        self.ui.setupUi(self)
        self.ui.btnCodificate.clicked.connect(self.btnCodificanteAction)
        self.ui.btnNoCodificante.clicked.connect(self.btnNoCodificanteAction)
        self.nombreArchivo = nombre
        self.ui.btnAmbos.clicked.connect(self.btnAmbosAction)
        self.resultadosNoCodificantes = ''
        self.resultadosCodificantes = ''

    def btnCodificanteAction(self):
        rangoQ = ''
        distancia = 1
        if self.ui.valorQ.currentText() != 'Seleccione una Opcion':
            if self.ui.valorQ.currentText() == '-1 a 1':
                rangoQ = np.arange(-1.0, 1.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3.0, 3.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5.0, 5 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10.0, 10+distancia, distancia)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20.0, 20 + distancia, distancia)
            I = imageio.imread(
                "Imagenes/Codificante/" + self.nombreArchivo + "_codificante.jpg")/255.0
            matriz = I[0:, 0:, 0]
            self.resultadosCodificantes = boxCounting.fractal_dimension(
                matriz, self.nombreArchivo + "Codificante", 'Codificante', distancia, rangoQ)
            pl.xlabel('q')
            pl.ylabel('H(q)')
            pl.title('q vs H(q)')
            pl.plot(rangoQ, self.resultadosCodificantes)
            pl.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def btnNoCodificanteAction(self):
        rangoQ = np.zeros(1)
        distancia = 1
        if self.ui.valorQ.currentText() != 'Seleccione una Opción':
            if self.ui.valorQ.currentText() == '-1 a 1':
                rangoQ = np.arange(-1.0, 1.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3.0, 3.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5.0, 5 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10.0, 10+distancia, distancia)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20.0, 20 + distancia, distancia)
            I = imageio.imread(
                "Imagenes/NoCodificante/" + self.nombreArchivo + "_noCodificante.jpg")/255.0
            matriz = I[0:, 0:, 0]
            self.resultadosNoCodificantes = boxCounting.fractal_dimension(
                matriz, self.nombreArchivo + "_noCodificante", 'NoCodificante', distancia, rangoQ)
            pl.xlabel('q')
            pl.ylabel('H(q)')
            pl.title('q vs H(q)')
            pl.plot(rangoQ, self.resultadosNoCodificantes)
            pl.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def btnAmbosAction(self):
        rangoQ = np.zeros(1)
        distancia = 1
        if self.ui.valorQ.currentText() != 'Seleccione una Opcion':
            if self.ui.valorQ.currentText() == '-1 a 1':
                rangoQ = np.arange(-1.0, 1.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3.0, 3.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5.0, 5 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10.0, 10+distancia, distancia)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20.0, 20 + distancia, distancia)
            I = imageio.imread(
                "Imagenes/Completa/" + self.nombreArchivo + "_completa.jpg")/255.0
            matriz = I[0:, 0:, 0]
            fq = boxCounting.fractal_dimension(
                matriz, self.nombreArchivo + "Completa", 'Completa', distancia, rangoQ)

            p1, p2, p3 = plot(rangoQ, self.resultadosCodificantes, 'r-',
                              rangoQ, self.resultadosNoCodificantes, 'b-', rangoQ, fq, 'g-')
            # Etiqueta del eje Y, que es común para todas
            pl.legend(('Left', 'Right', 'Center'),
                      prop={'size': 10}, loc='upper right')

            pl.xlabel('q')
            pl.ylabel('H(q)')
            pl.title('q vs H(q)')

            # Creo una figura (ventana), pero indico el tamaño (x,y) en pulgadas
            pl.savefig("boxCounting/Completa/" +
                       self.nombreArchivo + "_espectroqvshq.jpg")
            pl.show()
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
    mi_app = ventanaBoxCounting()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
