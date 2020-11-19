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
            self.analisisNoCodificante)
        self.nombreArchivo = nombre
        self.ui.btnAmbas.clicked.connect(self.mostrarImagen)
        self.rangoQCodificante = ''
        self.resultadosCodificante = ''
        self.rangoQNoCodificante = ''
        self.resultadosNoCodificante = ''
        self.rangoQCompleta = ''
        self.resultadosCompleta = ''
        self.resultadosFCodificantes = ''
        self.resultadosFNoCodificantes = ''
        self.resultadosFCompletos = ''
        self.rangoFCodificantes = ''
        self.rangoFNoCodificantes = ''
        self.rangoFCompletos = ''
        self.tqCodificante = ''
        self.tqNoCodificante = ''
        self.tqCompleta = ''
        self.graficaCodificante = False
        self.graficaNoCodificante = False

        # self.resize(pixmapNoCod.width(),pixmapNoCod.height())

    def imprimir(self):
        print('metodo')

    def mostrarImagen(self):
        if self.graficaCodificante and self.graficaNoCodificante:
            # array de valores a representar
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
                    rango1 = np.arange(-1.0, -0.5, distancia)
                    rango2 = np.arange(0.5, 1.0 + distancia, distancia)
                    rangoQ = np.concatenate((rango1, rango2), axis=0)
                elif self.ui.valorQ.currentText() == '-3 a 3':
                    rango1 = np.arange(-3.0, -0.5, distancia)
                    rango2 = np.arange(0.5, 3.0 + distancia, distancia)
                    rangoQ = np.concatenate((rango1, rango2), axis=0)
                elif self.ui.valorQ.currentText() == '-5 a 5':
                    rango1 = np.arange(-5.0, -0.5, distancia)
                    rango2 = np.arange(0.5, 5.0 + distancia, distancia)
                    rangoQ = np.concatenate((rango1, rango2), axis=0)
                elif self.ui.valorQ.currentText() == '-10 a 10':
                    rango1 = np.arange(-10.0, -0.5, distancia)
                    rango2 = np.arange(0.5, 10.0 + distancia, distancia)
                    rangoQ = np.concatenate((rango1, rango2), axis=0)
                elif self.ui.valorQ.currentText() == '-20 a 20':
                    rango1 = np.arange(-20.0, -0.5, distancia)
                    rango2 = np.arange(0.5, 20.0 + distancia, distancia)
                    rangoQ = np.concatenate((rango1, rango2), axis=0)

                data = detrended.lineaTiempo("ArchivosGenerados/Secuencias/Completa/" +
                                             self.nombreArchivo + "_completa.fasta")
                time = detrended.transformada(data)
                lag = detrended.divisiones(time, escalaSeleccionada)
                resultados = np.zeros(rangoQ.size)
                contenido = ''
                for i in range(0, rangoQ.size):
                    informacion = detrended.detrendedAnality(
                        time, lag, rangoQ[i], int(self.ui.lblGrado.text()))
                    resultados[i] = informacion['hurst']
                    contenido = contenido + \
                        informacion["titulo"] + informacion["contenido"] + \
                        "\n" + informacion["hurst_contenido"]
                archivo = open("ArchivosGenerados/Resultados/Completa/" +
                               self.nombreArchivo + "_completa.txt", "w")
                archivo.write(contenido)
                archivo.write("\n El valor del delta Q es: " +
                              str(max(resultados) - min(resultados)))
                archivo.close()
                self.rangoQCompleta = rangoQ
                self.resultadosCompleta = resultados
                self.rangoFCompletos, self.resultadosFCompletos, self.tqCompleta = detrended.fdealpha(
                    resultados, rangoQ, self.nombreArchivo + "_espectroCompleta.jpg")

                plt.xlabel('q')
                plt.ylabel('H(q)')
                plt.title('q vs H(q)')
                plt.plot(rangoQ, resultados, 'b-', label="Completa")
                plt.legend(
                    prop={'size': 10}, loc='upper right')
                plt.savefig("Imagenes/Graficas/Completa/" +
                            self.nombreArchivo + "_completa.jpg")
                plt.close()

                plt.xlabel('q')
                plt.ylabel('t(q)')
                plt.title('q vs t(q)')
                plt.plot(rangoQ, self.tqCompleta, "b-", label="Completa")
                plt.legend(
                    prop={'size': 10}, loc='upper right')
                plt.savefig("Imagenes/Graficas/qvstq/Completa/" +
                            self.nombreArchivo + "_tq_Completa")
                plt.close()

                plt.xlabel('q')
                plt.ylabel('t(q)')
                plt.title('q vs t(q)')

                plt.plot(rangoQ, self.tqCodificante, 'b-', label="Codificante")
                plt.plot(rangoQ, self.tqNoCodificante,
                         'r-', label="NoCodificante")
                plt.plot(rangoQ, self.tqCompleta, 'g-', label="Completa")
                plt.legend(
                    prop={'size': 10}, loc='upper right')
                plt.savefig("Imagenes/Graficas/qvstq/Todas/" +
                            self.nombreArchivo + "_tq_todas")
                plt.close()

            plt.subplot(121)
            p1, p2, p3 = plt.plot(self.rangoQCodificante, self.resultadosCodificante, 'b-',
                                  self.rangoQNoCodificante, self.resultadosNoCodificante, 'r-',
                                  self.rangoQCompleta, self.resultadosCompleta, 'g-')

            # Añado leyenda, tamaño de letra 10, en esquina superior derecha
            plt.legend(('Left', 'Right', 'Center'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')

            plt.savefig("Imagenes/Graficas/Ambas/" +
                        self.nombreArchivo + "_hqvq.jpg")

            plt.subplot(122)
            p1, p2, p3 = plt.plot(self.rangoFCodificantes, self.resultadosFCodificantes, 'b-',
                                  self.rangoFNoCodificantes, self.resultadosFNoCodificantes, 'r-',
                                  self.rangoFCompletos, self.resultadosFCompletos, 'g-')

            # Añado leyenda, tamaño de letra 10, en esquina superior derecha
            plt.legend(('Left', 'Right', 'Center'),
                       prop={'size': 10}, loc='upper right')

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.show()
            plt.savefig("Imagenes/Graficas/Ambas/" +
                        self.nombreArchivo + "_falpha.jpg")

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText(
                "Se debe generar la grafica codificante y no codificante")
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
                rango1 = np.arange(-1.0, -0.5, distancia)
                rango2 = np.arange(0.5, 1.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rango1 = np.arange(-3.0, -0.5, distancia)
                rango2 = np.arange(0.5, 3.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rango1 = np.arange(-5.0, -0.5, distancia)
                rango2 = np.arange(0.5, 5.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rango1 = np.arange(-10.0, -0.5, distancia)
                rango2 = np.arange(0.5, 10.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rango1 = np.arange(-20.0, -0.5, distancia)
                rango2 = np.arange(0.5, 20.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            data = detrended.lineaTiempo("ArchivosGenerados/Secuencias/NoCodificante/" +
                                         self.nombreArchivo + "_noCodificante.fasta")
            time = detrended.transformada(data)
            lag = detrended.divisiones(time, escalaSeleccionada)
            resultados = np.zeros(rangoQ.size)
            contenido = ''
            for i in range(0, rangoQ.size):
                informacion = detrended.detrendedAnality(
                    time, lag, rangoQ[i], int(self.ui.lblGrado.text()))
                resultados[i] = informacion['hurst']
                contenido = contenido + \
                    informacion["titulo"] + informacion["contenido"] + \
                    "\n" + informacion["hurst_contenido"]
            archivo = open("ArchivosGenerados/Resultados/NoCodificante/" +
                           self.nombreArchivo + "_noCodificante.txt", "w")
            archivo.write(contenido)
            archivo.write("\n El valor del delta Q es: " +
                          str(max(resultados) - min(resultados)))
            archivo.close()
            self.rangoQNoCodificante = rangoQ
            self.resultadosNoCodificante = resultados
            self.rangoFNoCodificantes, self.resultadosFNoCodificantes, self.tqNoCodificante = detrended.fdealpha(
                resultados, rangoQ, self.nombreArchivo + "_espectroNoCodificante.jpg")

            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, self.tqNoCodificante,
                     "b-", label="No Codificante")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("Imagenes/Graficas/qvstq/NoCodificante/" +
                        self.nombreArchivo + "_tq_NoCodificante")
            plt.close()

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')

            plt.plot(rangoQ, resultados, 'b-', label="No Codificante")
            plt.legend(
                prop={'size': 10}, loc='upper right')
            plt.savefig("Imagenes/Graficas/NoCodificante/" +
                        self.nombreArchivo + "_noCodificante.jpg")
            self.graficaNoCodificante = True
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
                rango1 = np.arange(-1.0, -0.5, distancia)
                rango2 = np.arange(0.5, 1.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rango1 = np.arange(-3.0, -0.5, distancia)
                rango2 = np.arange(0.5, 3.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rango1 = np.arange(-5.0, -0.5, distancia)
                rango2 = np.arange(0.5, 5.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rango1 = np.arange(-10.0, -0.5, distancia)
                rango2 = np.arange(0.5, 10.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rango1 = np.arange(-20.0, -0.5, distancia)
                rango2 = np.arange(0.5, 20.0 + distancia, distancia)
                rangoQ = np.concatenate((rango1, rango2), axis=0)
            data = detrended.lineaTiempo("ArchivosGenerados/Secuencias/Codificante/" +
                                         self.nombreArchivo + "_codificante.fasta")
            time = detrended.transformada(data)
            lag = detrended.divisiones(time, escalaSeleccionada)
            resultados = np.zeros(rangoQ.size)
            contenido = ''
            for i in range(0, rangoQ.size):
                informacion = detrended.detrendedAnality(
                    time, lag, rangoQ[i], int(self.ui.lblGrado.text()))
                resultados[i] = informacion['hurst']
                contenido = contenido + \
                    informacion['titulo'] + informacion['contenido'] + \
                    "\n" + informacion['hurst_contenido']
            archivo = open("ArchivosGenerados/Resultados/Codificante/" +
                           self.nombreArchivo + "_codificante.txt", "w")
            archivo.write(contenido)
            archivo.write("\n El valor del delta Q es: " +
                          str(max(resultados) - min(resultados)))
            archivo.close()
            self.rangoQCodificante = rangoQ
            self.resultadosCodificante = resultados
            self.rangoFCodificantes, self.resultadosFCodificantes, self.tqCodificante = detrended.fdealpha(
                resultados, rangoQ, self.nombreArchivo + "_espectroCodificante.jpg")

            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, self.tqCodificante, "b-", label="Codificante")
            plt.legend(
                prop={'size': 10}, loc='upper right')
            plt.savefig("Imagenes/Graficas/qvstq/Codificante/" +
                        self.nombreArchivo + "_tq_Codificante")

            plt.close()

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, resultados, 'b-', label="Codificante")
            plt.legend(
                prop={'size': 10}, loc='upper right')
            plt.savefig("Imagenes/Graficas/Codificante/" +
                        self.nombreArchivo + "_Codificante.jpg")
            self.graficaCodificante = True
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
    mi_app = ventanaDetrended()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
