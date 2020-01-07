from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from archivo import *

fondo="gray"
fuente = "Comic Sans MS"
tamano = 12

class Aplicacion:

    

    def __init__(self):
        self.ventana1=Tk()
        self.ventana1.title("Ventana Principal")
        miFrame = Frame()
        miFrame.pack(fill = "both", expand = "True")
        miFrame.config(bg = fondo)
        miFrame.config(width="650", height= "350")
        miFrame.config(bd=10)
        miFrame.config(relief = "groove")
        self.agregar_menu()
        #self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        #self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)      
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Cargar archivo", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)  

    def salir(self):
        sys.exit()


    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/home/juancho270",title = "Seleccione archivo",filetypes = (("fasta files","*.fasta"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            archivo1= Archivo()
            archivo1.leer(contenido)



aplicacion1=Aplicacion() 