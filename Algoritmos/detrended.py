# Imports
from MFDFA import MFDFA
from MFDFA import fgn
import numpy as np
import pylab as plt


class Detrended:
    def __init__(self):
        self.datos = ''

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
        for i in range(1, time.size):
            y[i] = y[i-1] + (time[i-1] - media)
        return y

    def divisiones(self, time, escala):
        segmento = time.size / escala
        lag = np.linspace(segmento, time.size, escala).astype(int)
        return lag

    def detrendedAnality(self, time, lag, q, order, nombre):
        lag, dfa = MFDFA(time, lag=lag, q=q, order=order)
        # To uncover the Hurst index, lets get some log-log plots
        # And now we need to fit the line to find the slope. We will
        # fit the first points, since the results are more accurate
        # there. Don't forget that if you are seeing in log-log
        # scales, you need to fit the logs of the results
        hurst = np.polyfit(np.log(lag[:15]), np.log(dfa[:15]), 1)[0]
        file = open(nombre, "a")
        file.write("Para q = " + str(q) + ": \n")
        for i in range(0, lag.size):
            file.write('Para la escala ' + str(i+1) + " " +
                       str(lag[i]) + ", " + "el valor DFA es: " + str(dfa[i]) + "\n")
        file.write("\n" + "\n")
        file.write("el valor de hurst es: " + str(hurst) + "\n")
        file.close()

        # Now what you should obtain is: slope = H + 1
        return hurst


detrended = Detrended()
