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
from numpy import array


class Archivo:
    def __init__(self):
        self.datos = ""
        self.tabla = ""
        self.codificante = ""
        self.nocodificante = ""
        self.cargaDatos = False
        self.cargaTabla = False
        self.nombreArchivo = ""

    def recuperar(self, ventana):
        nombrearch = QFileDialog.getOpenFileName(
            ventana, 'Open File', "", " (*.txt *.fasta *.fna )")

        if nombrearch[0] != '':
            archi1 = open(nombrearch[0], "r", encoding="utf-8")
            tamano = len(nombrearch[0].split('/'))
            self.nombreArchivo = nombrearch[0].split(
                '/')[tamano-1].split('.')[0]
            self.datos = (self.eliminarMarcas(archi1.read()))
            archi1.close()
            self.cargaDatos = True
        self.llamar()
        return nombrearch[0]

    def eliminarMarcas(self, contenidoArchivo):
        filas = contenidoArchivo.split('\n')
        lineaSecuencia = ''
        for i in filas:
            if i != '':
                if i[0] != '>':
                    lineaSecuencia = lineaSecuencia + \
                        self.quitarRepeticiones(i.upper(), 'N')
        return lineaSecuencia

    def recuperarTabla(self, ventana):
        nombrearch = QFileDialog.getOpenFileName(
            ventana, 'Open File', "", " (*.txt *.fasta )")
        if nombrearch[0] != '':
            self.tabla = pd.read_csv(nombrearch[0], sep='\t')
            self.cargaTabla = True
        self.llamar()
        return nombrearch[0]

    def llamar(self):
        if self.cargaTabla and self.cargaDatos:
            self.secuenciaDivididas()

    def secuenciaDivididas(self):
        obj1 = Secuencia(self.tabla, self.datos, self.nombreArchivo)
        obj1.separar()
        archi1 = open("ArchivosGenerados/Secuencias/Codificante/" +
                      self.nombreArchivo + "_codificante.fasta", "r", encoding="utf-8")
        contenido = archi1.read()
        self.codificante = contenido
        archi1.close()
        archi3 = open("ArchivosGenerados/Secuencias/NoCodificante/" +
                      self.nombreArchivo + "_noCodificante.fasta", "r", encoding="utf-8")
        contenido3 = archi3.read()
        self.no_codificante = contenido3
        archi3.close()

    def hacerImagenCodificante(self, nombre):
        T = imagen.chaos_game_representation2(self.codificante)
        plt.scatter(T[:, 0], T[:, 1], s=5 ** -
                    ((len(str(len(self.codificante))))-2), c='#000000')
        plt.axis('off')
        plt.savefig("Imagenes/Codificante/" + nombre + "_codificante" + ".jpg",
                    bbox_inches='tight', pad_inches=-0.2)
        plt.show()

    def hacerImagenNoCodificante(self, nombre):
        T = imagen.chaos_game_representation2(self.no_codificante)
        plt.scatter(T[:, 0], T[:, 1], s=5 ** -
                    ((len(str(len(self.no_codificante))))-2), c='#000000')
        plt.axis('off')
        plt.savefig("Imagenes/NoCodificante/" + nombre + "_noCodificante" +
                    ".jpg", bbox_inches='tight', pad_inches=-0.2)
        plt.show()

    def hacerImagenCompleta(self, nombre):
        T = imagen.chaos_game_representation2(self.datos)
        plt.scatter(T[:, 0], T[:, 1], s=5 ** -
                    ((len(str(len(self.datos))))-2), c='#000000')
        plt.axis('off')
        plt.savefig("Imagenes/Completa/" + nombre + "_completa" +
                    ".jpg", bbox_inches='tight', pad_inches=-0.2)
        plt.close()

    def quitarRepeticiones(self, unaCadena, unaLetra):
        cadena = ""
        for char in unaCadena:
            if(char != unaLetra):
                cadena = cadena+char
        return cadena


archivo = Archivo()
