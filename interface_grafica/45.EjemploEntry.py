from tkinter import *

root = Tk()

miFrame=Frame(root, width=600, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
#cuadroTexto.place(x=100, y=100) #Place sirve para posicion en pixeles
cuadroNombre.grid(row=0, column=1, padx= 10, pady= 10) #Grid posiciona en filas y columnas
cuadroNombre.config(fg= "blue", justify= "right")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1,padx = 10, pady= 10)
cuadroPass.config(show="*", fg= "red")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx= 10, pady= 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx= 10, pady= 10)

######################################################

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx= 10, pady= 10)

passLabel = Label(miFrame, text= "Contraseña: ")
passLabel.grid(row= 1, column= 0, padx= 10, pady= 10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

root.mainloop()
