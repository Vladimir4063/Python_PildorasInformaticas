from io import open

archivo_texto = open("archivo.txt", "r+") #Lectura y escritura

print(archivo_texto.read())

archivo_texto.seek(19) #seek : Vuelve el puntero a al lugar especificado

print(archivo_texto.read()) #tambien podemos especificar hasta donde debe leer, dandole un parametro en ()

print(archivo_texto.read(13)) 