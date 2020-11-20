import numpy as np
from archivo import *
from archivo import archivo
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Algoritmos.detrended2D import *
from detrend2D import *
from skimage import io
import matplotlib.pyplot as plt
import scipy.linalg
import math
import sys


class ventanaDetrended2D(QWidget):
    def __init__(self, parent, nombre):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_detrend2D()
        self.ui.setupUi(self)
        self.ui.btnCodificanteA.clicked.connect(
            self.analisisCodificante)
        self.ui.btnNoCodificanteA.clicked.connect(
            self.analisisNoCodificante)
        self.nombreArchivo = nombre
        self.ui.btnAmbas.clicked.connect(self.mostrarImagen)
        self.rangoQCodificante = ''
        self.resultadosCodificante = ''
        self.rangoQNoCodificante = ''
        self.resultadosNoCodificante = ''
        self.graficaCodificante = False
        self.graficaNoCodificante = False
        # self.resize(pixmapNoCod.width(),pixmapNoCod.height())

    def imprimir(self):
        print('metodo')

    def mostrarImagen(self):
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
                rangoQ = np.arange(-1.0, 1.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3.0, 3.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5.0, 5 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10.0, 10+distancia, distancia)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20.0, 20 + distancia, distancia)

            dataNoCodificante = io.imread(
                "Imagenes/NoCodificante/" + self.nombreArchivo + "_noCodificante.jpg")/255.0

            dataCodificante = io.imread(
                "Imagenes/Codificante/" + self.nombreArchivo + "_codificante.jpg")/255.0

            dataCompleta = io.imread(
                "Imagenes/Completa/" + self.nombreArchivo + "_completa.jpg")/255.0
            codificante = ''
            noCodificante = ''
            completa = ''
            if self.ui.empezarDesde.currentText() == 'Superior Derecha':
                codificante = dataCodificante
                noCodificante = dataNoCodificante
                completa = dataCompleta
            elif self.ui.empezarDesde.currentText() == 'Superior Izquierda':
                codificante = dataCodificante[::-1]
                noCodificante = dataNoCodificante[::-1]
                completa = dataCompleta[::-1]
            elif self.ui.empezarDesde.currentText() == 'Inferior Derecha':
                codificante = np.flip(dataCodificante)
                noCodificante = np.flip(dataNoCodificante)
                completa = np.flip(dataCompleta)
            else:
                codificante = np.flip(dataCodificante[::-1])
                noCodificante = np.flip(dataNoCodificante[::-1])
                completa = np.flip(dataCompleta[::-1])

            dataNoCodificante = detrended2D.convertirMatriz(noCodificante)
            dataCodificante = detrended2D.convertirMatriz(codificante)
            dataCompleta = detrended2D.convertirMatriz(completa)

            subconjuntosNoCodificante = detrended2D.subConjuntos(
                escalaSeleccionada, dataNoCodificante)
            subconjuntosCodificante = detrended2D.subConjuntos(
                escalaSeleccionada, dataCodificante)
            subconjuntosCompleta = detrended2D.subConjuntos(
                escalaSeleccionada, dataCompleta)

            sumAcomuladaNoCodificante = detrended2D.sumAcumuladaSubConjuntos(
                subconjuntosNoCodificante)
            sumAcomuladaCodificante = detrended2D.sumAcumuladaSubConjuntos(
                subconjuntosCodificante)
            sumAcomuladaCompleta = detrended2D.sumAcumuladaSubConjuntos(
                subconjuntosCompleta)

            covarianzaNoCodificante = detrended2D.calcularCovarianzaSubConjuntos(
                sumAcomuladaNoCodificante)
            covarianzaCodificante = detrended2D.calcularCovarianzaSubConjuntos(
                sumAcomuladaCodificante)
            covarianzaCompleta = detrended2D.calcularCovarianzaSubConjuntos(
                sumAcomuladaCompleta)

            funcionfNoCodificante = detrended2D.funcionf(
                sumAcomuladaNoCodificante, covarianzaNoCodificante)
            funcionfCodificante = detrended2D.funcionf(
                sumAcomuladaCodificante, covarianzaCodificante)
            funcionfSeqComplet = detrended2D.funcionf(
                sumAcomuladaCompleta, covarianzaCompleta)

            fluctuacionesCodificantes = detrended2D.funcionFluctuacion(
                rangoQ, funcionfCodificante)
            fluctuacionesNoCodificantes = detrended2D.funcionFluctuacion(
                rangoQ, funcionfNoCodificante)
            fluctuacionesSeqCompleta = detrended2D.funcionFluctuacion(
                rangoQ, funcionfSeqComplet)

            hCodificante, fCodificante, tqCodificante = detrended2D.graficarGuardar(
                fluctuacionesCodificantes, rangoQ, "Codificante/" + self.nombreArchivo + "_codificante")
            hNoCodificante, fNoCodificante, tqNoCodificante = detrended2D.graficarGuardar(
                fluctuacionesNoCodificantes, rangoQ, "NoCodificante/" + self.nombreArchivo + "_noCodificante")
            hSeqComplete, fSeqComplete, tqSeqComplete = detrended2D.graficarGuardar(
                fluctuacionesSeqCompleta, rangoQ, "SecuenciaCompleta/" + self.nombreArchivo + "_seqCompleta")
            # Figura con una fila y tres columnas, activo primer subgráfico
            plt.plot(rangoQ, tqCodificante)
            plt.plot(rangoQ, tqNoCodificante)
            plt.plot(rangoQ, tqSeqComplete)
            plt.legend(('SC', 'SNC', 'CC'),
                       prop={'size': 10}, loc='upper right')
            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.savefig("Detrended2D/graficah(q)vsq/qvstq/SecuenciaCompleta" +
                        self.nombreArchivo + "_secuenciaCompleta.jpg")
            plt.close()
            plt.subplot(121)
            p1, p2, p3 = plot(rangoQ, hCodificante, 'r-',
                              rangoQ, hNoCodificante, 'b-', rangoQ, hSeqComplete, 'g-')
            # Etiqueta del eje Y, que es común para todas
            plt.legend(('SC', 'SNC', 'CC'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')

            # Creo una figura (ventana), pero indico el tamaño (x,y) en pulgadas
            plt.savefig("Detrended2D/graficah(q)vsq/SecuenciaCompleta/" +
                        self.nombreArchivo + "_secuenciaCompleta.jpg")

            # Figura con una fila y tres columnas, activo segundo subgráfico
            plt.subplot(122)
            rangoQ2 = rangoQ[0:rangoQ.shape[0]-1]
            print(rangoQ.shape, rangoQ2.shape, fCodificante.shape)
            p4, p5, p6 = plot(rangoQ2, fCodificante, 'b-',
                              rangoQ2, fNoCodificante, 'r-', rangoQ2, fSeqComplete, 'g-')
            # Etiqueta del eje X, que es común para todas
            # Etiqueta del eje Y, que es común para todas
            plt.legend(('SC', 'SNC', 'CC'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            # Creo una figura (ventana), pero indico el tamaño (x,y) en pulgadas
            plt.savefig("Detrended2D/espectroMultifractal/SecuenciaCompleta/" +
                        self.nombreArchivo + "_secuenciaCompleta.jpg")

            plt.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def analisisNoCodificante(self):
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
                rangoQ = np.arange(-1.0, 1.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3.0, 3.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5.0, 5 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10.0, 10+distancia, distancia)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20.0, 20 + distancia, distancia)

            dataNoCodificante = io.imread(
                "Imagenes/NoCodificante/" + self.nombreArchivo + "_noCodificante.jpg")/255.0
            noCodificante = ''
            if self.ui.empezarDesde.currentText() == 'Superior Derecha':
                noCodificante = dataNoCodificante
            elif self.ui.empezarDesde.currentText() == 'Superior Izquierda':
                noCodificante = dataNoCodificante[::-1]
            elif self.ui.empezarDesde.currentText() == 'Inferior Derecha':
                noCodificante = np.flip(dataNoCodificante)
            else:
                noCodificante = np.flip(dataNoCodificante[::-1])
            data = detrended2D.convertirMatriz(noCodificante)
            subconjuntos = detrended2D.subConjuntos(escalaSeleccionada, data)
            sumAcomulada = detrended2D.sumAcumuladaSubConjuntos(subconjuntos)
            covarianza = detrended2D.calcularCovarianzaSubConjuntos(
                sumAcomulada)
            funcionf = detrended2D.funcionf(sumAcomulada, covarianza)
            fluctuaciones = detrended2D.funcionFluctuacion(rangoQ, funcionf)
            hNoCodificante, fNoCodificante = detrended2D.graficarGuardar(
                fluctuaciones, rangoQ, "NoCodificante/" + self.nombreArchivo + "_noCodificante")

            # Figura con una fila y tres columnas, activo primer subgráfico
            plt.subplot(121)
            p1,  = plot(rangoQ, hNoCodificante, 'r-')
            # Etiqueta del eje Y, que es común para todas
            plt.legend(('SNC'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')

            # Figura con una fila y tres columnas, activo segundo subgráfico
            plt.subplot(122)
            rangoQ2 = rangoQ[0:rangoQ.shape[0] - 1]
            p2 = plot(rangoQ2, fNoCodificante, 'b-')
            # Etiqueta del eje X, que es común para todas
            # Etiqueta del eje Y, que es común para todas
            plt.legend(('SNC'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

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
                rangoQ = np.arange(-1.0, 1.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3.0, 3.0 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5.0, 5 + distancia, distancia)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10.0, 10+distancia, distancia)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20.0, 20 + distancia, distancia)

            dataCodificante = io.imread(
                "Imagenes/Codificante/" + self.nombreArchivo + "_codificante.jpg")/255.0
            codificante = ''
            if self.ui.empezarDesde.currentText() == 'Superior Derecha':
                codificante = dataCodificante
            elif self.ui.empezarDesde.currentText() == 'Superior Izquierda':
                codificante = dataCodificante[::-1]
            elif self.ui.empezarDesde.currentText() == 'Inferior Derecha':
                codificante = np.flip(dataCodificante)
            else:
                codificante = np.flip(dataCodificante[::-1])

            data = detrended2D.convertirMatriz(codificante)
            subconjuntos = detrended2D.subConjuntos(escalaSeleccionada, data)
            sumAcomulada = detrended2D.sumAcumuladaSubConjuntos(subconjuntos)
            covarianza = detrended2D.calcularCovarianzaSubConjuntos(
                sumAcomulada)
            funcionf = detrended2D.funcionf(sumAcomulada, covarianza)
            fluctuaciones = detrended2D.funcionFluctuacion(rangoQ, funcionf)
            hCodificante, fCodificante = detrended2D.graficarGuardar(
                fluctuaciones, rangoQ, "Codificante/" + self.nombreArchivo + "_Codificante")

            # Figura con una fila y tres columnas, activo primer subgráfico
            plt.subplot(121)
            p1,  = plot(rangoQ, hCodificante, 'r-')
            # Etiqueta del eje Y, que es común para todas
            plt.legend(('SNC'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')

            # Figura con una fila y tres columnas, activo segundo subgráfico
            plt.subplot(122)
            rangoQ2 = rangoQ[0:rangoQ.shape[0] - 1]
            p2 = plot(rangoQ2, fCodificante, 'b-')
            print(rangoQ2, fCodificante)
            # Etiqueta del eje X, que es común para todas
            # Etiqueta del eje Y, que es común para todas
            plt.legend(('SNC'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.show()
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
    mi_app = ventanaDetrended2D()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
