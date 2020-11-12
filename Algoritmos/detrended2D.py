from skimage import io
import matplotlib.pyplot as plt
import scipy.linalg
import numpy as np
import math


class Detrended2D:
    def __init__(self):
        self.datos = ''
        self.Ms = 0
        self.Ns = 0
        self.s = 0

    def convertirMatriz(self, matriz):
        # Creamos matiz donde se guaradan los datos de los pixeles
        datos = np.zeros((matriz.shape[0], matriz.shape[1]))

        # llenamos la matriz con los datos de la imagen
        for i in range(0, matriz.shape[0]):
            for j in range(0, matriz.shape[1]):
                datos[i][j] = matriz[i][j][0]
        return datos

    def subConjuntos(self, s, matriz):
        self.Ms = math.floor(matriz.shape[0]/s)
        self.Ns = math.floor(matriz.shape[1]/s)
        self.s = s
        subconjuntos = np.zeros((self.Ms, self.Ns, s, s))
        for i in range(0, self.Ms):
            for j in range(0, self.Ns):
                subconjuntos[i][j] = matriz[i*s:(i*s) + s, j*s:(j*s) + s]
        return subconjuntos

    def sumAcumuladaSubConjuntos(self, matriz):
        sumSubconjuntos = np.zeros((self.Ms, self.Ns, self.s, self.s))
        for i in range(0, self.Ms):
            for j in range(0, self.Ns):
                suma = 0
                for l in range(0, self.s):
                    for k in range(0, self.s):
                        suma = suma + matriz[i][j][l][k]
                        sumSubconjuntos[i][j][l][k] = suma
        return sumSubconjuntos

    def calcularCovarianzaSubConjuntos(self, matriz):
        covarianzaSubconjuntos = np.zeros((self.Ms, self.Ns, self.s, self.s))
        for k in range(0, self.Ms):
            for l in range(0, self.Ns):
                zline = np.zeros(self.s*self.s)
                xline = np.zeros(self.s*self.s)
                yline = np.zeros(self.s*self.s)
                count = 0
                for i in range(0, self.s):
                    for j in range(0, self.s):
                        xline[count] = i
                        yline[count] = j
                        zline[count] = matriz[k][l][i][j]
                        count = count + 1
                # Data for a three-dimensional line
                A = np.c_[xline, yline, np.ones(xline.shape)]
                C, _, _, _ = scipy.linalg.lstsq(A, zline)    # coefficients
                # evaluate it on grid
                Z = C[0]*xline + C[1]*yline + C[2]
                covarianzaSubconjuntos[k][l] = Z.reshape((self.s, self.s))
        return covarianzaSubconjuntos

    """ def funcionF2Img(self, sumSubconjuntosx, sumSubconjuntosy, covarianzaSubConjuntosx, covarianzaSubConjuntosy):
        F = np.zeros((self.Ms, self.Ns))
        for k in range(0, self.Ms):
            for l in range(0, self.Ns):
                count = 0
                for i in range(0, self.s):
                    for j in range(0, self.s):
                        count = count + \
                            (abs(sumSubconjuntosx[k][l][i][j] - covarianzaSubConjuntosx[k][l][i][j]) * abs(
                                sumSubconjuntosy[k][l][i][j] - covarianzaSubConjuntosy[k][l][i][j]))
                F[k][l] = (1/self.s**2) * count
        return F """

    def funcionf(self, sumSubconjuntos, covarianzaSubConjuntos):
        F = np.zeros((self.Ms, self.Ns))
        for k in range(0, self.Ms):
            for l in range(0, self.Ns):
                count = 0
                for i in range(0, self.s):
                    for j in range(0, self.s):
                        count = count + (sumSubconjuntos[k][l][i][j] -
                                         covarianzaSubConjuntos[k][l][i][j])
                F[k][l] = (1/self.s**2) * count
        return F

    def funcionFluctuacion(self, q, F):
        valores = np.zeros(q.shape)
        posicion = 0
        for i in q:
            count = 0
            for j in range(0, self.Ms):
                for k in range(0, self.Ns):
                    if i != 0:
                        count = count + ((abs(F[j][k]))**(i/2))
                    else:
                        count = count + math.log(abs(F[j][k]))
            if i != 0:
                valores[posicion] = ((1/(self.Ms*self.Ns)) * count)**(1/i)
            else:
                valores[posicion] = math.exp((1/(2*self.Ms*self.Ns)) * count)
            posicion = posicion + 1
        return valores

    def graficarGuardar(self, valores, q, nombre):
        valoresFinales = np.zeros(q.shape)
        countFinal = 0

        for i in valores:
            valoresFinales[countFinal] = abs(math.log(i)/math.log(self.s))
            countFinal = countFinal + 1

        plt.plot(q, valoresFinales, 'b-', label="SC")

        plt.savefig("Detrended2D/graficah(q)vsq/" +
                    nombre + "_graficaq.jpg")
        plt.close()
        file = open("Detrended2D/Resultados/" +
                    nombre + "_resultados.txt", 'w')
        for i in range(0, q.shape[0]):
            file.write(
                "\n Para q = " + str(q[i]) + ",el valor DFA es:" + str(valoresFinales[i]))
        file.write("\n El delta Q es: " +
                   str(max(valoresFinales) - min(valoresFinales)))
        file.close()
        valoresFinales2 = np.zeros(q.shape[0] - 1)
        tq = np.zeros(q.shape)
        posicionFinal = 0
        for i in q:
            tq[posicionFinal] = (i * valoresFinales[posicionFinal]) - 2
            posicionFinal = posicionFinal + 1
        plt.plot(q, tq, 'b-')
        plt.xlabel('q')
        plt.ylabel('tq')
        plt.title('q vs tq')
        plt.savefig("Detrended2D/qvstq/" +
                    nombre + "_tqvsq.jpg")
        plt.close()
        derivadaHq = np.diff(tq)/(q[1]-q[0])
        index = -1
        for i in range(0, (q.shape[0])-1):
            index = index + 1
            valoresFinales2[index] = q[i]*derivadaHq[index] - tq[index]
        q2 = q[0:q.shape[0]-1]
        plt.plot(q2, valoresFinales2, 'b-')
        plt.savefig("Detrended2D/espectroMultifractal/" +
                    nombre + "_espectro.jpg")
        plt.close()

        return valoresFinales, valoresFinales2


detrended2D = Detrended2D()
