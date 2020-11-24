import sys
from boxCounting import *
from Algoritmos.multCT_JVBoxCounting import readfasta
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
        self.DeltaCodificante = "No Caloculado"
        self.DeltaNoCodificante = "No Calculado"
        self.DeltaCompleto = "No calculado"

    def btnCodificanteAction(self):
        rangoQ = ''
        if self.ui.valorQ.currentText() != 'Seleccione una Opción':
            if self.ui.valorQ.currentText() == '-1 a 1':
                rangoQ = np.arange(-1, 2, 1)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3, 4, 1)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5, 6, 1)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10, 11, 1)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20, 21, 1)
            ruta = "ArchivosGenerados/Secuencias/Codificante/" + \
                self.nombreArchivo + "_codificante.fasta"
            # Se calcula el espectro con el ejecutable de boxCounting
            info = readfasta(ruta)
            # Se separa la info
            datos = info.split(" ")
            # Se crea una lista de tuplas para guardar la info
            arreglo = np.zeros((41, 2))
            # Vector para guardar las respuestas segun el rango
            dq = np.zeros(rangoQ.shape[0])
            contador = 0
            indice = -20
            # Se recorren los datos del espectro
            for i in datos[1].split("\t"):
                if i != '':
                    arreglo[contador][0] = indice
                    arreglo[contador][1] = i
                    contador = contador + 1
                    indice = indice + 1

            valorq = 0
            for i in rangoQ:
                for j in arreglo:
                    if i == j[0]:
                        dq[valorq] = j[1]
                        valorq = valorq + 1
            # Guarda los datos del Hq para cada q
            archivo1 = open("BoxCounting/Resultados/Codificante/" +
                            self.nombreArchivo + ".txt", "w")
            for i in range(0, rangoQ.shape[0]):
                archivo1.write(
                    "Para el valor q = " + str(rangoQ[i]) + ", el valor Hq es: " + str(dq[i]) + "\n")
            archivo1.write("El valor delta de Q es:" + str(max(dq)-min(dq)))
            archivo1.close()
            self.DeltaCodificante = str(round(max(dq)-min(dq), 3))
            self.ui.DeltaCod.setText(self.DeltaCodificante)
            # Se calcula el valor de tq para cada q
            tq = np.zeros(rangoQ.shape[0])
            for i in range(0, rangoQ.shape[0]):
                tq[i] = (rangoQ[i]*dq[i]) - 1
            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, tq, 'b-', label="SC")
            plt.legend(prop={'size': 10}, loc='lower right')
            plt.savefig("BoxCounting/qvstq/Codificante/" +
                        self.nombreArchivo + ".jpg")
            plt.close()
            # Se calcula al funcion f
            f = np.zeros(rangoQ.shape[0] - 1)
            diff = np.diff(tq)/(rangoQ[1]-rangoQ[0])
            for i in range(0, rangoQ.shape[0] - 1):
                f[i] = rangoQ[i]*diff[i] - tq[i]

            rangoQespecial = np.delete(rangoQ, rangoQ.shape[0]-1)
            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, f, 'b-', label="SC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig(
                "BoxCounting/espectroMultifractal/Codificante/" + self.nombreArchivo + ".jpg")
            plt.close()
            # Se grafica q vs Hq
            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dq, 'b-', label="SC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/graficah(q)vsq/Codificante/" +
                        self.nombreArchivo + ".jpg")
            plt.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def btnNoCodificanteAction(self):
        rangoQ = ''
        if self.ui.valorQ.currentText() != 'Seleccione una Opción':
            if self.ui.valorQ.currentText() == '-1 a 1':
                rangoQ = np.arange(-1, 2, 1)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3, 4, 1)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5, 6, 1)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10, 11, 1)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20, 21, 1)
            ruta = "ArchivosGenerados/Secuencias/NoCodificante/" + \
                self.nombreArchivo + "_noCodificante.fasta"
            # Se calcula el espectro con el ejecutable de boxCounting
            info = readfasta(ruta)
            # Se separa la info
            datos = info.split(" ")
            # Se crea una lista de tuplas para guardar la info
            arreglo = np.zeros((41, 2))
            # Vector para guardar las respuestas segun el rango
            dq = np.zeros(rangoQ.shape[0])
            contador = 0
            indice = -20
            # Se recorren los datos del espectro
            for i in datos[1].split("\t"):
                if i != '':
                    arreglo[contador][0] = indice
                    arreglo[contador][1] = i
                    contador = contador + 1
                    indice = indice + 1

            valorq = 0
            for i in rangoQ:
                for j in arreglo:
                    if i == j[0]:
                        dq[valorq] = j[1]
                        valorq = valorq + 1
            # Guarda los datos del Hq para cada q
            archivo1 = open("BoxCounting/Resultados/NoCodificante/" +
                            self.nombreArchivo + ".txt", "w")
            for i in range(0, rangoQ.shape[0]):
                archivo1.write(
                    "Para el valor q = " + str(rangoQ[i]) + ", el valor Hq es: " + str(dq[i]) + "\n")
            archivo1.write("El valor delta de Q es:" + str(max(dq)-min(dq)))
            archivo1.close()
            self.DeltaNoCodificante = str(round(max(dq)-min(dq), 3))
            self.ui.DeltaNoCod.setText(self.DeltaNoCodificante)
            # Se calcula el valor de tq para cada q
            tq = np.zeros(rangoQ.shape[0])
            for i in range(0, rangoQ.shape[0]):
                tq[i] = (rangoQ[i]*dq[i]) - 1
            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, tq, 'b-', label="SNC")
            plt.legend(prop={'size': 10}, loc='lower right')
            plt.savefig("BoxCounting/qvstq/NoCodificante/" +
                        self.nombreArchivo + ".jpg")
            plt.close()
            # Se calcula al funcion f
            f = np.zeros(rangoQ.shape[0] - 1)
            diff = np.diff(tq)/(rangoQ[1]-rangoQ[0])
            for i in range(0, rangoQ.shape[0] - 1):
                f[i] = rangoQ[i]*diff[i] - tq[i]

            rangoQespecial = np.delete(rangoQ, rangoQ.shape[0]-1)
            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, f, 'b-', label="SNC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig(
                "BoxCounting/espectroMultifractal/NoCodificante/" + self.nombreArchivo + ".jpg")
            plt.close()
            # Se grafica q vs Hq
            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dq, 'b-', label="SNC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/graficah(q)vsq/NoCodificante/" +
                        self.nombreArchivo + ".jpg")
            plt.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Faltan Selecciones")
            msg.setInformativeText(
                "Se debe seleccionar el rango para q, la escala y el grado, y la distancia debe ser un flotante")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def btnAmbosAction(self):
        rangoQ = ''
        if self.ui.valorQ.currentText() != 'Seleccione una Opción':
            if self.ui.valorQ.currentText() == '-1 a 1':
                rangoQ = np.arange(-1, 2, 1)
            elif self.ui.valorQ.currentText() == '-3 a 3':
                rangoQ = np.arange(-3, 4, 1)
            elif self.ui.valorQ.currentText() == '-5 a 5':
                rangoQ = np.arange(-5, 6, 1)
            elif self.ui.valorQ.currentText() == '-10 a 10':
                rangoQ = np.arange(-10, 11, 1)
            elif self.ui.valorQ.currentText() == '-20 a 20':
                rangoQ = np.arange(-20, 21, 1)
            rutaSC = "ArchivosGenerados/Secuencias/Codificante/" + \
                self.nombreArchivo + "_codificante.fasta"
            rutaSNC = "ArchivosGenerados/Secuencias/NoCodificante/" + \
                self.nombreArchivo + "_noCodificante.fasta"
            rutaCC = "ArchivosGenerados/Secuencias/Completa/" + \
                self.nombreArchivo + "_completa.fasta"
            # Se calcula el espectro con el ejecutable de boxCounting
            infoSC = readfasta(rutaSC)
            infoSNC = readfasta(rutaSNC)
            infoCC = readfasta(rutaCC)
            # Se separa la info
            datosSC = infoSC.split(" ")
            datosSNC = infoSNC.split(" ")
            datosCC = infoCC.split(" ")
            # Se crea una lista de tuplas para guardar la info
            arregloSC = np.zeros((41, 2))
            arregloSNC = np.zeros((41, 2))
            arregloCC = np.zeros((41, 2))
            # Vector para guardar las respuestas segun el rango
            dqSC = np.zeros(rangoQ.shape[0])
            dqSNC = np.zeros(rangoQ.shape[0])
            dqCC = np.zeros(rangoQ.shape[0])
            contadorSC = 0
            indiceSC = -20
            contadorSNC = 0
            indiceSNC = -20
            contadorCC = 0
            indiceCC = -20
            # Se recorren los datos del espectro
            for i in datosSC[1].split("\t"):
                if i != '':
                    arregloSC[contadorSC][0] = indiceSC
                    arregloSC[contadorSC][1] = i
                    contadorSC = contadorSC + 1
                    indiceSC = indiceSC + 1
            for i in datosSNC[1].split("\t"):
                if i != '':
                    arregloSNC[contadorSNC][0] = indiceSNC
                    arregloSNC[contadorSNC][1] = i
                    contadorSNC = contadorSNC + 1
                    indiceSNC = indiceSNC + 1
            for i in datosCC[1].split("\t"):
                if i != '':
                    arregloCC[contadorCC][0] = indiceCC
                    arregloCC[contadorCC][1] = i
                    contadorCC = contadorCC + 1
                    indiceCC = indiceCC + 1

            valorq = 0
            for i in rangoQ:
                for j in range(0, arregloSC.shape[0]):
                    if i == arregloSC[j][0]:
                        dqSC[valorq] = arregloSC[j][1]
                        dqSNC[valorq] = arregloSNC[j][1]
                        dqCC[valorq] = arregloCC[j][1]
                        valorq = valorq + 1
            # Guarda los datos del Hq para cada q
            archivo1 = open("BoxCounting/Resultados/Codificante/" +
                            self.nombreArchivo + ".txt", "w")
            archivo2 = open("BoxCounting/Resultados/NoCodificante/" +
                            self.nombreArchivo + ".txt", "w")
            archivo3 = open("BoxCounting/Resultados/SecuenciaCompleta/" +
                            self.nombreArchivo + ".txt", "w")
            for i in range(0, rangoQ.shape[0]):
                archivo1.write(
                    "Para el valor q = " + str(rangoQ[i]) + ", el valor Hq es: " + str(dqSC[i]) + "\n")
                archivo2.write(
                    "Para el valor q = " + str(rangoQ[i]) + ", el valor Hq es: " + str(dqSNC[i]) + "\n")
                archivo3.write(
                    "Para el valor q = " + str(rangoQ[i]) + ", el valor Hq es: " + str(dqCC[i]) + "\n")
            archivo1.write("El valor delta de Q es:" +
                           str(max(dqSC)-min(dqSC)))
            archivo2.write("El valor delta de Q es:" +
                           str(max(dqSNC)-min(dqSNC)))
            archivo3.write("El valor delta de Q es:" +
                           str(max(dqCC)-min(dqCC)))
            archivo1.close()
            archivo2.close()
            archivo3.close()
            self.DeltaCodificante = str(round(max(dqSC)-min(dqSC), 3))
            self.ui.DeltaCod.setText(self.DeltaCodificante)
            self.DeltaNoCodificante = str(round(max(dqSNC)-min(dqSNC), 3))
            self.ui.DeltaNoCod.setText(self.DeltaNoCodificante)
            self.DeltaCompleto = str(round(max(dqCC)-min(dqCC), 3))
            self.ui.DeltaCom.setText(self.DeltaCompleto)
            # Se calcula el valor de tq para cada q
            tqSC = np.zeros(rangoQ.shape[0])
            tqSNC = np.zeros(rangoQ.shape[0])
            tqCC = np.zeros(rangoQ.shape[0])
            for i in range(0, rangoQ.shape[0]):
                tqSC[i] = (rangoQ[i]*dqSC[i]) - 1
                tqSNC[i] = (rangoQ[i]*dqSNC[i]) - 1
                tqCC[i] = (rangoQ[i]*dqCC[i]) - 1
            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, tqSC, 'b-', label="SC")
            plt.legend(prop={'size': 10}, loc='lower right')
            plt.savefig("BoxCounting/qvstq/Codificante/" +
                        self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, tqSNC, 'b-', label="SNC")
            plt.legend(prop={'size': 10}, loc='lower right')
            plt.savefig("BoxCounting/qvstq/NoCodificante/" +
                        self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, tqCC, 'b-', label="CC")
            plt.legend(prop={'size': 10}, loc='lower right')
            plt.savefig("BoxCounting/qvstq/SecuenciaCompleta/" +
                        self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('q')
            plt.ylabel('t(q)')
            plt.title('q vs t(q)')
            plt.plot(rangoQ, tqSC, 'r-', label="SC")
            plt.plot(rangoQ, tqSNC, 'b-', label="SNC")
            plt.plot(rangoQ, tqCC, 'g-', label="CC")
            plt.legend(prop={'size': 10}, loc='lower right')
            plt.savefig("BoxCounting/qvstq/Ambas/" +
                        self.nombreArchivo + ".jpg")
            plt.close()
            # Se calcula al funcion f
            fCC = np.zeros(rangoQ.shape[0] - 1)
            fSC = np.zeros(rangoQ.shape[0] - 1)
            fSNC = np.zeros(rangoQ.shape[0] - 1)
            diffCC = np.diff(tqCC)/(rangoQ[1]-rangoQ[0])
            diffSC = np.diff(tqSC)/(rangoQ[1]-rangoQ[0])
            diffSNC = np.diff(tqSNC)/(rangoQ[1]-rangoQ[0])
            for i in range(0, rangoQ.shape[0] - 1):
                fCC[i] = rangoQ[i]*diffCC[i] - tqCC[i]
                fSC[i] = rangoQ[i]*diffSC[i] - tqSC[i]
                fSNC[i] = rangoQ[i]*diffSNC[i] - tqSNC[i]

            rangoQespecial = np.delete(rangoQ, rangoQ.shape[0]-1)
            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, fSC, 'b-', label="SC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig(
                "BoxCounting/espectroMultifractal/Codificante/" + self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, fSNC, 'b-', label="SNC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig(
                "BoxCounting/espectroMultifractal/NoCodificante/" + self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, fCC, 'b-', label="CC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig(
                "BoxCounting/espectroMultifractal/SecuenciaCompleta/" + self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, fSC, 'r-', label="SC")
            plt.plot(rangoQespecial, fSNC, 'b-', label="SNC")
            plt.plot(rangoQespecial, fCC, 'g-', label="CC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/espectroMultifractal/Ambas/" +
                        self.nombreArchivo + ".jpg")
            plt.close()
            # Se grafica q vs Hq
            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dqSC, 'b-', label="SC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/graficah(q)vsq/Codificante/" +
                        self.nombreArchivo + ".jpg")
            plt.close()

            # Se grafica q vs Hq
            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dqSNC, 'b-', label="SNC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/graficah(q)vsq/NoCodificante/" +
                        self.nombreArchivo + ".jpg")
            plt.close()

            # Se grafica q vs Hq
            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dqCC, 'b-', label="CC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/graficah(q)vsq/SecuenciaCompleta/" +
                        self.nombreArchivo + ".jpg")
            plt.close()

            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dqSC, 'r-', label="SC")
            plt.plot(rangoQ, dqSNC, 'b-', label="SNC")
            plt.plot(rangoQ, dqCC, 'g-', label="CC")
            plt.legend(prop={'size': 10}, loc='upper right')
            plt.savefig("BoxCounting/graficah(q)vsq/Ambas/" +
                        self.nombreArchivo + ".jpg")
            plt.close()
            # Se juntan las secuencias
            plt.subplot(121)
            plt.xlabel('q')
            plt.ylabel('H(q)')
            plt.title('q vs H(q)')
            plt.plot(rangoQ, dqSC, 'r-', label="SC")
            plt.plot(rangoQ, dqSNC, 'b-', label="SNC")
            plt.plot(rangoQ, dqCC, 'g-', label="CC")
            plt.legend(prop={'size': 10}, loc='upper right')

            plt.subplot(122)
            plt.xlabel('α')
            plt.ylabel('f(α)')
            plt.title('α vs f(α)')
            plt.plot(rangoQespecial, fSC, 'r-', label="SC")
            plt.plot(rangoQespecial, fSNC, 'b-', label="SNC")
            plt.plot(rangoQespecial, fCC, 'g-', label="CC")
            plt.legend(prop={'size': 10}, loc='upper right')

            plt.savefig("BoxCounting/Juntas/" + self.nombreArchivo + ".jpg")
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
    mi_app = ventanaBoxCounting()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
