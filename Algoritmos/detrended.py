# Imports
from MFDFA import MFDFA
from MFDFA import fgn
import numpy as np
import pylab as plt


class Detrended:
    def __init__(self):
        self.datos = ''
        self.order = 0

    def lineaTiempo(self, name):
        archivo = open(name, "r")
        contenido = archivo.read()
        archivo.close()
        data = []
        for char in contenido:
            if char == 'A':
                data.append(1.)
            elif char == 'T':
                data.append(2.)
            elif char == 'G':
                data.append(3.)
            elif char == 'C':
                data.append(4.)
        time = np.array(data)
        return time

    def transformada(self, time):
        media = time.mean()

        y = np.zeros([time.size])
        # Integrate the process
        y[0] = (time[0] - media)
        for i in range(1, time.size):
            y[i] = y[i-1] + (time[i-1] - media)
        return y

    def divisiones(self, time, escala):
        segmento = time.size / escala
        lag = np.linspace(segmento, time.size, escala).astype(int)
        return lag

    def detrendedAnality(self, time, lag, q, order):
        self.order = order
        lag, dfa = MFDFA(time, lag=lag, q=q, order=order)
        # To uncover the Hurst index, lets get some log-log plots
        # And now we need to fit the line to find the slope. We will
        # fit the first points, since the results are more accurate
        # there. Don't forget that if you are seeing in log-log
        # scales, you need to fit the logs of the results
        data = {}
        data["contenido"] = ''
        hurst = np.polyfit(np.log(lag[:15]), np.log(dfa[:15]), 1)[0]
        data["hurst"] = hurst
        data["titulo"] = "Para q = " + str(q) + ": \n"
        for i in range(0, lag.size):
            data["contenido"] = data["contenido"] + "Para la escala " + str(i+1) + " " + str(
                lag[i]) + ", " + "el valor DFA es: " + str(dfa[i]) + "\n"
        data["hurst_contenido"] = "el valor de hurst es: " + str(hurst) + "\n"
        return data

    # Definicion de F de alpha
    def fdealpha(self, valoresFinales, q, nombre):
        valoresFinales2 = np.zeros(q.shape[0] - 1)
        tq = np.zeros(q.shape)
        posicionFinal = 0
        for i in q:
            tq[posicionFinal] = (i * valoresFinales[posicionFinal]) - 1
            posicionFinal = posicionFinal + 1

        derivadaHq = np.diff(tq)/(q[1]-q[0])
        index = -1
        for i in range(0, (q.shape[0])-self.order):
            index = index + 1
            valoresFinales2[index] = abs(q[i]*derivadaHq[index] - tq[index])

        posicion = np.where(valoresFinales2 == np.amax(valoresFinales2))
        valoresFinales3 = np.delete(valoresFinales2, posicion)
        q2 = np.delete(q, posicion)[0:q.shape[0]-2]

        plt.xlabel('α')
        plt.ylabel('f(α)')
        plt.title('α vs f(α)')
        plt.show()
        plt.plot(q2, valoresFinales3, 'b-')
        plt.savefig("Imagenes/Graficas/Espectro/" +
                    nombre)
        plt.close()

        return q2, valoresFinales3, tq


detrended = Detrended()
