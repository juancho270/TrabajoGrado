import pylab
import math
from six.moves import xrange
from random import choice
from numpy import array


class Imagen:
    def __init__(self):
        print("")

    def chaos_game_representation2(self, secuencia):
        A = (0., 0.)
        T = (1., 0.)
        G = (1., 1.)
        C = (0., 1.)

        V = [A, T, G, C]
        p0 = (0.5, 0.5)
        arreglo = [p0]

        def pmedio(x, y):
            return (0.5*(x[0] + y[0]), 0.5*(x[1] + y[1]))

        for i in secuencia:
            vact = V[0]
            if i.upper() == 'A':
                vact = V[0]
            elif i.upper() == 'T':
                vact = V[1]
            elif i.upper() == 'G':
                vact = V[2]
            elif i.upper() == 'C':
                vact = V[3]
            pact = arreglo[-1]
            psig = pmedio(pact, vact)
            arreglo.append(psig)

        arreglo = array(arreglo)
        return arreglo


imagen = Imagen()
