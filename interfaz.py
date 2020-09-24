from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from archivo import *
from archivo import *
from tkinter import messagebox


class Aplicacion:

    def __init__(self):
        self.ventana1 = Tk()
        self.ventana1.title("Ventana Principal")
        self.ventana1.resizable(width=False, height=False)
        self.var = IntVar()
        self.rutaArchivo = StringVar()
        self.rutaTabla = StringVar()
        self.fuente = "Comic Sans MS"
        self.tamano = 12
        self.fondoComponentes = "steelBlue3"
        self.carga = False
        self.cargaTabla = False
        miFrame = Frame()
        miFrame.pack(fill="both", expand="True")
        miFrame.config(width="650", height="450")
        miFrame.config(bd=10)
        miFrame.config(bg="mint cream")

        self.labelArchivo = ""
        self.labelTabla = ""
        self.agregar_menu()
        self.agregar_opciones()
        #self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        #self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Cargar archivo", command=self.copiar)
        opciones1.add_command(label="Cargar Tabla", command=self.tabla)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

    def copiar(self):
        ruta = archivo.recuperar()
        self.rutaArchivo.set(ruta)
        self.carga = True

    def tabla(self):
        ruta = archivo.recuperarTabla()
        self.rutaTabla.set(ruta)
        self.cargaTabla = True

    def agregar_opciones(self):
        botonCodificante = Button(self.ventana1, text="Imagen \n Codificante",
                                  command=self.siguiente, bg=self.fondoComponentes, width=10, height=2)

        botonCodificante.place(x=550, y=350)
        botonNoCodificante = Button(self.ventana1, text="Imagen \n  No Codificante",
                                    command=self.noCodificante, bg=self.fondoComponentes, width=12,  height=2)
        botonNoCodificante.place(x=450, y=350)
        botonSalir = Button(self.ventana1, text="Salir",
                            command=self.salir, bg=self.fondoComponentes, width=10, height=2)
        botonSalir.place(x=350, y=350)

        labelKmers = Label(self.ventana1, text="# K-mers: ").place(x=10, y=25)

        archivoLabel = Label(self.ventana1, text="Ruta Archivo:")
        archivoLabel.place(x=10, y=125)
        self.labelArchivo = Entry(
            self.ventana1, state="readonly", textvariable=self.rutaArchivo, width=70)
        self.labelArchivo.place(x=100, y=125)
        self.rutaArchivo.set("Seleccione un archivo")
        btnArchivo = Button(self.ventana1, text="Cargar",
                            command=self.copiar, bg=self.fondoComponentes, width=10)
        btnArchivo.place(x=550, y=120)

        tablaLabel = Label(self.ventana1, text="Ruta Tabla:")
        tablaLabel.place(x=10, y=150)
        self.labelTabla = Entry(
            self.ventana1, state="readonly", textvariable=self.rutaTabla, width=70)
        self.labelTabla.place(x=100, y=150)
        self.rutaTabla.set("Seleccione una tabla")
        btnTabla = Button(self.ventana1, text="Cargar",
                          command=self.tabla, bg=self.fondoComponentes, width=10)
        btnTabla.place(x=550, y=150)

        selectorKmers = Scale(self.ventana1, from_=1, to=6, orient=HORIZONTAL,
                              bg=self.fondoComponentes, variable=self.var)
        selectorKmers.place(x=100, y=25)

    def siguiente(self):
        if self.carga and self.cargaTabla:
            kmers = self.var.get()
            archivo.hacerImagenCodificante(kmers)
        else:
            messagebox.showinfo(
                message="Por favor cargue un archivo en formato fasta y una tabla de coordenadas", title="Archivo no Cargado")

    def noCodificante(self):
        if self.carga and self.cargaTabla:
            kmers = self.var.get()
            archivo.hacerImagenNoCodificante(kmers)
        else:
            messagebox.showinfo(
                message="Por favor cargue un archivo en formato fasta y una tabla de coordenadas", title="Archivo no Cargado")

    def salir(self):
        sys.exit()


aplicacion1 = Aplicacion()
