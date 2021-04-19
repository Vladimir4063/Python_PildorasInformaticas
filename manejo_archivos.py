from io import open

archivo_texto=open("archivo.txt", "a")
 

#archivo_texto.write(frase)

#Debemos cerrar la manipulacion del archivo en memoria
#archivo_texto.close()

lineas_texto = archivo_texto.readlines()

#Agregamos un texto
#archivo_texto.write("\n Ahora si funciono.")

archivo_texto.close()

print(lineas_texto[0])