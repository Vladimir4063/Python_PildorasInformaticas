from tkinter import *

root = Tk()
root.geometry('300x300')

barraMenu = Menu(root)
root.config(menu=barraMenu)

#Contenido a las solapas
#tearoff/elimina lagrima
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Abrir Nuevo")
#Separador
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")

#Edition
archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Deshacer")
archivoEdicion.add_command(label="Rehacer")
archivoEdicion.add_command(label="Formato")

#Tools
archivoHerramientas = Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Avanzado")
#Help
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Soporte")
archivoAyuda.add_command(label="Documentacion")

#Solapas de menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
