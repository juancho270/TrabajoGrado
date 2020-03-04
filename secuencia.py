import pandas as pd
import os

class Secuencia:
    def __init__(self,tabla,secuencia):
        self.data=secuencia
        self.df = tabla
        self.codificante = ""
        self.no_codificante = ""
        self.columnas = len(self.df.index)

    def separar(self):
    	for i in range(len(self.df.index)):
    		if self.df['# feature'][i] == 'gene':
    			if self.df['strand'][i] == '+':
    				self.codificante = self.codificante + (self.data[self.df['start'][i]: self.df['end'][i]])
    			else:
    				self.codificante = self.codificante + (self.data[self.df['start'][i]: self.df['end'][i]])[:: - 1 ]
    			if i != len(self.df.index):
    				if self.df['strand'][i] == '+':
    					self.no_codificante = self.no_codificante + (self.data[self.df['end'][i]:self.df['start'][i+1]])
    				else:
    					self.no_codificante = self.no_codificante + (self.data[self.df['end'][i]:self.df['start'][i+1]])[:: - 1 ]
    			else:
    				if self.df['end'][i] != len(self.data):
    					if self.df['strand'][i] == '+':
    						self.no_codificante = self.no_codificante + (self.data[self.df['end'][i]:len(self.data)])
    					else:
    						self.no_codificante = self.no_codificante + (self.data[self.df['end'][i]:len(self.data)])
    	self.almacenar()

    def almacenar(self):
    	file = open("/home/usuario/Escritorio/TrabajoGrado/codificante.fasta","w")
    	file.write(self.codificante)
    	file2 = open("/home/usuario/Escritorio/TrabajoGrado/no_codificante.fasta","w")
    	file2.write(self.no_codificante)
    	file.close()
    	file2.close()





