import pandas as pd
import os


class Secuencia:
    def __init__(self, tabla, secuencia, nombre):
        self.data = secuencia
        self.df = tabla
        self.nombreArchivo = nombre
        self.codificante = ""
        self.no_codificante = ""
        self.columnas = len(self.df.index)

    def separar(self):
        if os.path.isfile("ArchivosGenerados/Secuencias/Codificante/" + self.nombreArchivo + "_codificante.fasta") == False and os.path.isfile("ArchivosGenerados/Secuencias/NoCodificante/" + self.nombreArchivo + "_noCodificante.fasta") == False and os.path.isfile("ArchivosGenerados/Secuencias/Completa/" + self.nombreArchivo + "_completa.fasta") == False:
            tablaCromosoma = self.filtrarTabla().reset_index(drop=True)
            for i in range(len(tablaCromosoma.index)):
                if i == 0:
                    if tablaCromosoma['start'][i] == 0 or tablaCromosoma['start'][i] == 1:
                        if tablaCromosoma['strand'][i] == '+':
                            self.codificante = self.codificante + \
                                (self.data[tablaCromosoma['start'][i]                                           : tablaCromosoma['end'][i]]).upper()
                        else:
                            self.codificante = self.codificante + \
                                (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]])[
                                    :: - 1].upper()
                    else:
                        if tablaCromosoma['strand'][i] == '+':
                            self.no_codificante = self.no_codificante + \
                                (self.data[0:tablaCromosoma['start'][i]]).upper()
                            self.codificante = self.codificante + \
                                (self.data[tablaCromosoma['start'][i]                                           : tablaCromosoma['end'][i]]).upper()
                        else:
                            self.no_codificante = self.no_codificante + \
                                (self.data[0:tablaCromosoma['start'][i]])[
                                    :: - 1].upper()
                            self.codificante = self.codificante + \
                                (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]])[
                                    :: - 1].upper()
                else:
                    if i == len(tablaCromosoma.index):
                        if tablaCromosoma['end'][i] == len(self.data):
                            if tablaCromosoma['strand'][i] == '+':
                                self.no_codificante = self.no_codificante + \
                                    (self.data[tablaCromosoma['end'][i-1]:tablaCromosoma['start'][i]]).upper()
                                self.codificante = self.codificante + \
                                    (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]]).upper()
                            else:
                                self.no_codificante = self.no_codificante + \
                                    (self.data[tablaCromosoma['end'][i-1]:tablaCromosoma['start'][i]])[:: -1].upper()
                                self.codificante = self.codificante + \
                                    (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]])[
                                        :: -1].upper()
                        else:
                            if tablaCromosoma['strand'][i] == '+':
                                self.codificante = self.codificante + \
                                    (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]]).upper()
                                self.no_codificante = self.no_codificante + \
                                    (self.data[tablaCromosoma['end'][i-1]:tablaCromosoma['start'][i]]).upper()
                                self.no_codificante = self.no_codificante + \
                                    (self.data[tablaCromosoma['end']
                                               [i]: len(self.data)]).upper()
                            else:
                                self.no_codificante = self.no_codificante + \
                                    (self.data[tablaCromosoma['end'][i-1]:tablaCromosoma['start'][i]])[:: -1].upper()
                                self.codificante = self.codificante + \
                                    (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]])[
                                        :: -1].upper()
                                self.no_codificante = self.no_codificante + \
                                    (self.data[tablaCromosoma['end'][i]: len(self.data)])[
                                        :: -1].upper()
                    else:
                        if tablaCromosoma['strand'][i] == '+':
                            self.no_codificante = self.no_codificante + \
                                (self.data[tablaCromosoma['end'][i-1]:tablaCromosoma['start'][i]]).upper()
                            self.codificante = self.codificante + \
                                (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]]).upper()
                        else:
                            self.no_codificante = self.no_codificante + \
                                (self.data[tablaCromosoma['end'][i-1]:tablaCromosoma['start'][i]])[:: -1].upper()
                            self.codificante = self.codificante + \
                                (self.data[tablaCromosoma['start'][i]: tablaCromosoma['end'][i]])[
                                    :: -1].upper()
            self.almacenar()
        else:
            file = open("ArchivosGenerados/Secuencias/Codificante/" +
                        self.nombreArchivo + "_codificante.fasta", "r")
            self.codificante = file.read()
            file.close()
            file2 = open("ArchivosGenerados/Secuencias/NoCodificante/" +
                         self.nombreArchivo + "_noCodificante.fasta", "r")
            self.no_codificante = file2.read()
            file2.close()

    def filtrarTabla(self):
        tablaCromosoma = self.df[(self.df['# feature'] == 'gene') & (
            self.df['seq_type'] == 'chromosome')]
        return tablaCromosoma

    def almacenar(self):
        file = open("ArchivosGenerados/Secuencias/Codificante/" +
                    self.nombreArchivo + "_codificante.fasta", "w")
        file.write(self.codificante)
        file2 = open("ArchivosGenerados/Secuencias/NoCodificante/" +
                     self.nombreArchivo + "_noCodificante.fasta", "w")
        file2.write(self.no_codificante)
        file3 = open("ArchivosGenerados/Secuencias/Completa/" +
                     self.nombreArchivo + "_completa.fasta", "w")
        file3.write(self.data)
        file.close()
        file2.close()
        file3.close()
