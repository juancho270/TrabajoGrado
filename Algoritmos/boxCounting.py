import numpy as np
import imageio
import pylab as pl


class BoxCounting:
    def __init__(self,):
        self.datos = ''

    def rgb2gray(self, rgb):
        r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray

    def fractal_dimension(self, Z, name, carpeta, threshold=0.8, ):
        # Only for 2d image
        assert(len(Z.shape) == 2)

        # From https://github.com/rougier/numpy-100 (#87)

        def boxcount(Z, k):
            S = np.add.reduceat(
                np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                np.arange(0, Z.shape[1], k), axis=1)

            # We count non-empty (0) and non-full boxes (k*k)
            return len(np.where((S > 0) & (S < k*k))[0])

        # Transform Z into a binary array
        Z = (Z < threshold)

        # Minimal dimension of image
        p = min(Z.shape)

        # Greatest power of 2 less than or equal to p
        n = 2**np.floor(np.log(p)/np.log(2))

        # Extract the exponent
        n = int(np.log(n)/np.log(2))

        # Build successive box sizes (from 2**n down to 2**1)
        sizes = 2**np.arange(n, 1, -1)
        print('sizes: ', sizes)
        # Actual box counting with decreasing size
        counts = []
        for size in sizes:
            print('valor k:   ', size)
            counts.append(boxcount(Z, size))
        np.savetxt("boxCounting/" + carpeta + "/" + name +
                   "_scaling.txt", list(zip(sizes, counts)))

        # Fit the successive log(sizes) with log (counts)
        print('counts: ', counts)
        coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
        pl.plot(np.log(sizes), np.log(counts), 'o', mfc='none')
        pl.plot(np.log(sizes), np.polyval(coeffs, np.log(sizes)))
        pl.xlabel('log $\epsilon$')
        pl.ylabel('log N')
        pl.savefig("boxCounting/" + carpeta + "/" +
                   name + "_sierpinski_dimension.pdf")
        pl.close()
        return -coeffs[0]


boxCounting = BoxCounting()
