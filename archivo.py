import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from imagen import *


class Archivo:
    def __init__(self):
        self.datos = ""

    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/home/juancho270/escritorio",title = "Seleccione archivo",filetypes = (("fasta files","*.fasta"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            contenido2  ="".join(contenido.split("\n")[ 1 :])
            self.datos= self.quitarRepeticiones(contenido2,'N')
            archi1.close()

            

    def hacerImagen(self,kmers):
        f2 = imagen.count_kmers(self.datos,kmers)
        print("contadores: \n")
        print(f2)
        f2_prob = imagen.probabilities(self.datos,f2,kmers)
        print("probabilidad: \n")
        print(f2_prob)
        chaos_f2 = imagen.chaos_game_representation(f2_prob,kmers)
        pylab.title('Chaos game representation for' + str(kmers) + '-mers')
        pylab.imshow(chaos_f2, interpolation='nearest', cmap=cm.gray_r)
        pylab.show()

    def quitarRepeticiones(self,unaCadena,unaLetra):
        cadena=""
        for char in unaCadena:
            if(char!=unaLetra):
                 cadena=cadena+char
        return cadena
 
archivo = Archivo()