from tkinter import *

root = Tk()
root.geometry("200x120")

varOpcion = IntVar() #Aqui se estara guardando el valor del radioButton

def imprimir(): #Obtendra el valir seleccionado, e imprimira por consola.
    #print(varOpcion.get())
    if varOpcion.get() == 1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get() == 2:
        etiqueta.config(text="Has elegido femenino.")
    else:
        etiqueta.config(text="Has elegido otra opc.")
    

Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

Radiobutton(root, text="Otra opc.", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
