import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class Archivo:
    def __init__(self):
        print("hola")

  

    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/home/juancho270/escritorio",title = "Seleccione archivo",filetypes = (("fasta files","*.fasta"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.leer(contenido)

     
    def leer(self, contenido):
        print(contenido)
 
archivo = Archivo()