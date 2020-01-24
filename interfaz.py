from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from archivo import *


class Aplicacion:

    def __init__(self):
        self.ventana1=Tk()
        self.ventana1.title("Ventana Principal")
        self.ventana1.resizable(width=False, height=False)
        self.var = IntVar()
        self.fondo="dodgerblue"
        self.fuente = "Comic Sans MS"
        self.tamano = 12
        self.fondoComponentes = "gray"
        miFrame = Frame()
        miFrame.pack(fill = "both", expand = "True")
        miFrame.config(bg = self.fondo)
        miFrame.config(width="450", height= "300")
        miFrame.config(bd=10)
        miFrame.config(relief = "groove")
        self.agregar_menu()
        self.agregar_opciones()
        #self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        #self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)      
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Cargar archivo", command=archivo.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)  

    def agregar_opciones(self):
    	botonSiguiente= Button(self.ventana1,text="Siguiente",command=self.siguiente, bg=self.fondoComponentes).place(x=340,y=250)
    	botonSalir = Button(self.ventana1,text="Salir",command= self.salir, bg=self.fondoComponentes).place(x=280,y=250)
    	labelKmers = Label(self.ventana1,text="# K-mers: ", bg=self.fondoComponentes).place(x=10,y=25)
    	selectorKmers = Scale(self.ventana1, from_=1, to=4,orient=HORIZONTAL, bg=self.fondoComponentes,variable=self.var).place(x=80,y=25)
    
    def siguiente(self):
    	self.ventana2=Tk()
    	self.ventana2.title("Imagenes") 
    	kmers= self.var.get()
    	print(kmers)   


    def salir(self):
        sys.exit()


aplicacion1=Aplicacion() 