from tkinter import *

fondo="gray"
fuente = "Comic Sans MS"
tamano = 12
#Creacion y configuracion de la ventana principal

ventana1=Tk()
ventana1.title("Ventana Principal")
#ventana1.resizable(1,1)
#ventana1.geometry("650x300")
ventana1.config(bg="blue")

#FRAME
miFrame = Frame()
miFrame.pack(fill = "both", expand = "True")
miFrame.config(bg = fondo)
miFrame.config(width="650", height= "350")
miFrame.config(bd=10)
miFrame.config(relief = "groove")
#miFrame.config(cursor="hand2")

#Widgets
cargarLabel = Label(miFrame,text="Cargar", font=(fuente,tamano))
cargarLabel.config(bg=fondo)
cargarLabel.place(x=25, y=25)
ventana1.mainloop()

