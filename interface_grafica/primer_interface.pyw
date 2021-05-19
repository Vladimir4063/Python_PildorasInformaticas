from tkinter import *

raiz=Tk()

raiz.title("Primer ventana")

raiz.resizable(1,0) #De esta forma solo puedo expandir a los lados. Si ambos fueran 0 o False, no se podria agrandar. (width, heigth)

raiz.config(bg ="red")

raiz.geometry("400x400")

raiz.mainloop()