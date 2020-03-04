from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from archivo import *
from tkinter import messagebox


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
        self.carga = False
        miFrame = Frame()
        miFrame.pack(fill = "both", expand = "True")
        miFrame.config(width="450", height= "300")
        miFrame.config(bd=10)
        miFrame.config(relief = "groove")
        self.labelArchivo = ""
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
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)  


    def copiar(self):
        archivo.recuperar()
        self.labelArchivo = Label(self.ventana1,text="Archivo cargado exitosamente!!",bg="green").place(x=10,y=125)
        self.carga = True


    def agregar_opciones(self):
        botonSiguiente= Button(self.ventana1,text="Siguiente",command=self.siguiente, bg=self.fondoComponentes).place(x=340,y=250)    
        botonSalir = Button(self.ventana1,text="Salir",command= self.salir, bg=self.fondoComponentes).place(x=280,y=250)
        labelKmers = Label(self.ventana1,text="# K-mers: ", bg=self.fondoComponentes).place(x=10,y=25)
        self.labelArchivo=Label(self.ventana1,text="Archivo no cargado",bg="red").place(x=10,y=125)
        selectorKmers = Scale(self.ventana1, from_=1, to=6,orient=HORIZONTAL, bg=self.fondoComponentes,variable=self.var).place(x=80,y=25)
    
    def siguiente(self):
        if self.carga:
            kmers= self.var.get()
            archivo.hacerImagen(kmers)
        else:
        	messagebox.showinfo(message="Por favor cargue un archivo en formato fasta", title="Archivo no Cargado")

    	  


    def salir(self):
        sys.exit()


aplicacion1=Aplicacion() 
