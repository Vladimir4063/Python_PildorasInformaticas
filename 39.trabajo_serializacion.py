import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("39.1.lista_nombres", "wb") #El segundo parametro es el permiso que damos. Seria, Write and Binary 

"Volcamos la lista"
pickle.dump(lista_nombres, fichero_binario) #El primero parametro es la lista, el segundo es el dato en memoria.

#Cerramos el fichero.
fichero_binario.close()

#Borramos de la memoria.
del(fichero_binario)