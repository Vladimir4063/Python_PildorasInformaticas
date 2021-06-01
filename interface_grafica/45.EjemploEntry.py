from tkinter import *

root = Tk()

miFrame=Frame(root, width=600, height=600)
miFrame.pack()

minombre= StringVar() #Indicamos que se trata de una cadena de caracteres

cuadroNombre = Entry(miFrame, textvariable=minombre) #Caja esta asociada al disparo de la variable
#cuadroTexto.place(x=100, y=100) #Place sirve para posicion en pixeles
cuadroNombre.grid(row=0, column=1, padx= 10, pady= 10) #Grid posiciona en filas y columnas
cuadroNombre.config(fg= "blue", justify= "right") #config permite editar elemento

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1,padx = 10, pady= 10)
cuadroPass.config(show="*", fg= "red")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx= 10, pady= 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx= 10, pady= 10)

cuadroComentarios = Text(miFrame, width=16, height= 5) #Text = add comentary
cuadroComentarios.grid(row=4, column=1, padx= 10, pady= 10)

scrollVert = Scrollbar(miFrame, command=cuadroComentarios.yview) #Scroll de la caja.
scrollVert.grid(row=4, column=2, sticky= "nsew")

cuadroComentarios.config(yscrollcommand= scrollVert.set) #Hability Scroll
######################################################

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx= 10, pady= 10)

passLabel = Label(miFrame, text= "Contraseña: ")
passLabel.grid(row= 1, column= 0, padx= 10, pady= 10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10) #Sticky posiciona segun puntos cardinales

direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, padx= 10, pady= 10)

#######################################################

def enviarNombre():
    minombre.set("Vladimir")

Btt1 = Button(miFrame, text= "Enviar", command=enviarNombre)
Btt1.grid(row=5, column=1)
#Btt1.pack()


#Btt2 = Button(miFrame, text= "Cancelar")
#Btt2.grid(row=5, column=2)

root.mainloop()
