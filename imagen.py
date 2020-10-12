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

    def count_kmers(self, sequence, k):
        d = collections.defaultdict(int)
        for i in xrange(len(sequence)-(k-1)):
            d[sequence[i:i+k]] += 1
        return d

    def probabilities(self, sequence, kmer_count, k):
        probabilities = collections.defaultdict(float)
        N = len(sequence)
        for key, value in kmer_count.items():
            probabilities[key] = float(value) / (N - k + 1)
        return probabilities

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

    def chaos_game_representation(self, probabilities, k):
        array_size = int(math.sqrt(4**k))
        chaos = []
        for i in range(array_size):
            chaos.append([0]*array_size)
        maxx = array_size
        maxy = array_size
        posx = 1
        posy = 1
        for key, value in probabilities.items():
            for char in key:
                if char == "T":
                    posx += maxx / 2
                elif char == "C":
                    posy += maxy / 2
                elif char == "G":
                    posx += maxx / 2
                    posy += maxy / 2
                maxx = maxx / 2
                maxy /= 2
            chaos[int(posy)-1][int(posx)-1] = value
            maxx = array_size
            maxy = array_size
            posx = 1
            posy = 1

        return chaos


imagen = Imagen()
