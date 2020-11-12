import collections
from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import cm
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

        # Intentar:
        # Poner vertices directamente
        # Poner más vértices (tener cuidado con el choice)
        #
        V = [A, T, G, C]
        p0 = (0.5, 0.5)
        arreglo = [p0]

        # Intentar
        # Definición de punto medio con def
        # ¿Qué pasa si no es el punto medio?
        #
        def pmedio(x, y): return (0.5*(x[0] + y[0]), 0.5*(x[1] + y[1]))
        # Poner esto hasta arriba
        #
        for i in secuencia:
            # Intentar
            # Definición propia de random
            #
            vact = V[0]
            if i == 'A':
                vact = V[0]
            elif i == 'T':
                vact = V[1]
            elif i == 'G':
                vact = V[2]
            elif i == 'C':
                vact = V[3]
            pact = arreglo[-1]
            psig = pmedio(pact, vact)
            arreglo.append(psig)

        # for p in T:
        #   print("{0} \t {1}".format(p[0],p[1]))

        arreglo = array(arreglo)
        return arreglo


imagen = Imagen()
