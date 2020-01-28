import collections
from collections import OrderedDict
from matplotlib import pyplot as plt
from matplotlib import cm
import pylab
import math
from six.moves import xrange

class Imagen:
    def __init__(self):
        print("")

    def count_kmers(self,sequence, k):
        d = collections.defaultdict(int)
        for i in xrange(len (sequence)-(k-1)):
            d[sequence[i:i+k]] +=1
        return d

    def probabilities(self,sequence,kmer_count, k):
    	probabilities = collections.defaultdict(float)
    	N = len(sequence)
    	for key, value in kmer_count.items():
    		probabilities[key] = float(value) / (N - k + 1)
    	return probabilities


    def chaos_game_representation(self,probabilities, k):
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