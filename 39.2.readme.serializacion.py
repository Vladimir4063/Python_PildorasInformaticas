#importamos library
import pickle

fichero = open("39.1.lista_nombres", "rb")


#Load = Cargar info. de ->
lista = pickle.load(fichero)

print(lista)