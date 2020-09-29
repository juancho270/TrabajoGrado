import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from imagen import *
import pandas as pd
from secuencia import *
from PyQt5.QtWidgets import *
from pylab import *
import matplotlib.pyplot as plt


class Archivo:
    def __init__(self):
        self.datos = ""
        self.tabla = ""
        self.codificante = ""
        self.nocodificante = ""
        self.cargaDatos = False
        self.cargaTabla = False

    def recuperar(self, ventana):
        nombrearch = QFileDialog.getOpenFileName(
            ventana, 'Open File', "", " (*.txt *.fasta )")
        if nombrearch != '':
            archi1 = open(nombrearch[0], "r", encoding="utf-8")
            contenido = archi1.read()
            contenido2 = "".join(contenido.split("\n")[1:])
            self.datos = self.quitarRepeticiones(contenido2, 'N')
            archi1.close()
            self.cargaDatos = True
        self.llamar()
        return nombrearch[0]

    def recuperarTabla(self, ventana):
        nombrearch = QFileDialog.getOpenFileName(
            ventana, 'Open File', "", " (*.txt *.fasta )")
        if nombrearch != '':
            self.tabla = pd.read_csv(nombrearch[0], sep='\t')
            self.cargaTabla = True
        self.llamar()
        return nombrearch[0]

    def llamar(self):
        if self.cargaTabla and self.cargaDatos:
            self.secuenciaDivididas()

    def secuenciaDivididas(self):
        obj1 = Secuencia(self.tabla, self.datos)
        obj1.separar()
        archi1 = open("codificante.fasta", "r", encoding="utf-8")
        contenido = archi1.read()
        self.codificante = contenido
        archi1.close()
        archi3 = open("no_codificante.fasta", "r", encoding="utf-8")
        contenido3 = archi3.read()
        self.no_codificante = contenido3
        archi3.close()

    def hacerImagenCodificante(self, kmers):
        f2 = imagen.count_kmers(self.codificante, kmers)
        print("contadores: \n")
        print(f2)
        f2_prob = imagen.probabilities(self.codificante, f2, kmers)
        print("probabilidad: \n")
        print(f2_prob)
        chaos_f2 = imagen.chaos_game_representation(f2_prob, kmers)
        plt.imshow(chaos_f2, interpolation='nearest', cmap=cm.gray_r)
        plt.axis('off')
        plt.savefig("Codificante.jpg", bbox_inches='tight',
                    pad_inches=0, dpi=300)
        plt.show()

    def hacerImagenNoCodificante(self, kmers):
        f2 = imagen.count_kmers(self.no_codificante, kmers)
        print("contadores: \n")
        print(f2)
        f2_prob = imagen.probabilities(self.no_codificante, f2, kmers)
        print("probabilidad: \n")
        print(f2_prob)
        chaos_f2 = imagen.chaos_game_representation(f2_prob, kmers)
        plt.imshow(chaos_f2, interpolation='nearest', cmap=cm.gray_r)
        plt.axis('off')
        plt.savefig("noCodificante.jpg", bbox_inches='tight',
                    pad_inches=0, dpi=300)
        plt.show()

    def quitarRepeticiones(self, unaCadena, unaLetra):
        cadena = ""
        for char in unaCadena:
            if(char != unaLetra):
                cadena = cadena+char
        return cadena


archivo = Archivo()
