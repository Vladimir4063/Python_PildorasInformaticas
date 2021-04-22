from io import open

#formas de uso : w-r-a

archivo_texto=open("archivo.txt", "a")
 

#archivo_texto.write(frase)

#Debemos cerrar la manipulacion del archivo en memoria
#archivo_texto.close()

lineas_texto = archivo_texto.readlines() #lee una linea

#Agregamos un texto
#archivo_texto.write("\n Ahora si funciono.")

archivo_texto.close()

print(lineas_texto[0])