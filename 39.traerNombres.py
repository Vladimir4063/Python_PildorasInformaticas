import pickle

fichero=open("39.lista_nombres", "rb") #read binary

lista=pickle.load(fichero)

print(lista)