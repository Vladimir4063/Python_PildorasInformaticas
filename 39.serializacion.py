import pickle

lista_nombres= ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("39.lista_nombres", "wb") #"E"scritura "B"inaria

pickle.dump(lista_nombres, fichero_binario) #Requiere dos argumentos: 1 info que vuelcas, 2 fichero donde quieres guardar

fichero_binario.close()

del(fichero_binario)