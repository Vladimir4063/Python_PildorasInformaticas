import pickle
"""
Este archivo no corre correctamente debido a que no conoce la clase "Vehiculos"
y mucho menos el atributo "estado"

Para poder correr correctamente, se debe pegar la clase unicamente. "Vehiculo y propiedades"
"""
ficheroApertura=open("40.loscoches", "rb")

misCoches=pickle.load(ficheroApertura) #Vuelco la lectura binaria

ficheroApertura.close() #close arch

for c in misCoches:

    print(c.estado())