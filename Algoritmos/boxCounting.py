import numpy as np
import imageio
import pylab as pl
import math


class BoxCounting:
    def __init__(self,):
        self.datos = ''
        self.pixelesTotales = 0

    def fractal_dimension(self, Z, name, carpeta, distancia, rangoQ):
        # Only for 2d image
        assert(len(Z.shape) == 2)

        # From https://github.com/rougier/numpy-100 (#87)
        def contarPixeles(self, matriz):
            for i in range(0, matriz.shape[0]):
                for j in range(0, matriz.shape[1]):
                    self.pixelesTotales = self.pixelesTotales + matriz[i][j]

        def boxcountFP(Z, k, q):
            # se divide la imagen en la escala k y se suma cada division
            S = np.add.reduceat(np.add.reduceat(Z, np.arange(
                0, Z.shape[0], k), axis=0), np.arange(0, Z.shape[1], k), axis=1)
            suma = 0

            # se recorre las sumas de las divisiones y se suman elevando al valor de q para q!=1
            for i in range(0, S.shape[0]):
                for j in range(0, S.shape[1]):
                    if S[i][j] != 0:
                        if q != 1:
                            suma = suma + ((S[i][j]/self.pixelesTotales)**q)
                        else:
                            suma = suma + \
                                math.log(S[i][j]/self.pixelesTotales)
            return (np.log(suma)/(q-1))

        # Transform Z into a binary array

        # Minimal dimension of image
        p = min(Z.shape)

        # Greatest power of 2 less than or equal to p
        n = 2**np.floor(np.log(p)/np.log(2))
        # Extract the exponent
        n = int(np.log(n)/np.log(2))

        # Build successive box sizes (from 2**n down to 2**1)
        sizes = 2**np.arange(n, 1, -1)
        Z = (Z <= 0.5)
        # Actual box counting with decreasing size

        distancia = distancia
        q = np.arange(-10.0, 10.0 + distancia, distancia)
        fq = np.zeros(sizes.shape)
        datos = np.zeros(q.shape)
        print(sizes)
        for i in range(0, q.shape[0]):
            if q[i] != 1:
                for j in range(0, sizes.shape[0]):
                    fq[j] = boxcountFP(Z, sizes[j], q[i])
                valor = np.polyfit(-np.log(1/sizes), fq, 1)
                # pl.plot(-np.log(1/sizes), fq)
                datos[i] = valor[0]
            else:
                datos[i] = datos[i-1] - 0.001
        pl.xlabel('q')
        pl.ylabel('H(q)')
        pl.title('q vs H(q)')
        print(q, datos)
        pl.plot(q, datos)
        pl.savefig("boxCounting/" + carpeta + "/" +
                   name + "_espectroqvshq.jpg")
        pl.close()
        return datos


boxCounting = BoxCounting()
