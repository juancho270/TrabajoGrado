import numpy as np
import imageio
import pylab as pl


class BoxCounting:
    def __init__(self,):
        self.datos = ''

    def fractal_dimension(self, Z, name, carpeta, distancia, rangoQ):
        # Only for 2d image
        assert(len(Z.shape) == 2)

        # From https://github.com/rougier/numpy-100 (#87)

        def boxcount(Z, k):
            S = np.add.reduceat(
                np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                np.arange(0, Z.shape[1], k), axis=1)

            # We count non-empty (0) and non-full boxes (k*k)
            return len(np.where((S > 0) & (S <= k*k))[0])

        def boxcountFP(Z, k, q):
            S = np.add.reduceat(np.add.reduceat(Z, np.arange(
                0, Z.shape[0], k), axis=0), np.arange(0, Z.shape[1], k), axis=1)
            suma = 0
            cuadros = 0
            for i in range(0, S.shape[0]):
                for j in range(0, S.shape[1]):
                    if S[i][j] == 0:
                        cuadros = cuadros+1
                    else:
                        suma = suma + S[i][j]**q
            return (np.log(suma / ((Z.shape[0]*Z.shape[1]) - cuadros)))/(q-1)

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
        counts = []
        for size in sizes:
            counts.append(boxcount(Z, size))
        np.savetxt("boxCounting/" + carpeta + "/" + name +
                   "_scaling.txt", list(zip(sizes, counts)))

        # Fit the successive log(sizes) with log (counts)
        coeffs = np.polyfit(-np.log(1/sizes), np.log(counts), 1)
        pl.plot(-np.log(1/sizes), np.log(counts), 'o', mfc='none')
        pl.plot(-np.log(1/sizes), np.polyval(coeffs, np.log(sizes)))
        pl.xlabel('-Ln I')
        pl.ylabel('log N(I)')
        pl.savefig("boxCounting/" + carpeta + "/" +
                   name + "_sierpinski_dimension.pdf")
        pl.close()
        print("The Hausdorff dimension is", -coeffs[0])
        pl.close()

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
                datos[i] = -coeffs[0]
        pl.xlabel('q')
        pl.ylabel('H(q)')
        pl.title('q vs H(q)')
        print(q, datos[::-1])
        pl.plot(q, datos[::-1])
        pl.show()
        pl.savefig("boxCounting/" + carpeta + "/" +
                   name + "_espectroqvshq.jpg")
        return -coeffs[0], datos[::-1]


boxCounting = BoxCounting()
