from tkinter import *

raiz=Tk()

raiz.title("Primer ventana")
raiz.resizable(1,1) #De esta forma solo puedo expandir a los lados. Si ambos fueran 0 o False, no se podria agrandar. (width, heigth)
raiz.config(bg ="blue")
#raiz.geometry("400x400")
raiz.config(bd=40) #Grosor de borde
raiz.config(relief="sunken") #tipo de borde
raiz.config(cursor="hand2") # tipo de cursor


miFrame=Frame()
#miFrame.pack(side="right", anchor="s") #Indicamos posicion fija
miFrame.pack(fill="y", expand=True)
miFrame.config(bg ="pink") #color de fondo
miFrame.config(width="650", height="350")
miFrame.config(bd=34) #tamaño de borde
miFrame.config(relief="groove") #tipo de borde
miFrame.config(cursor="pirate") #tipo de cursor

raiz.mainloop()