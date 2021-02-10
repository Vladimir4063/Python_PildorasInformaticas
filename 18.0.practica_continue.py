
for letra in "Python":
    if letra == "h":
        continue #Ignora proxima linea, y empieza de nuevo el While
    
    print("Viendo la letra: " + letra)
    
#_____________________________________

nombre= "pildoras inforamticas"

contador = 0

for i in nombre:
    if i ==" ":
        continue
    contador+=1

print("contador "+str(contador)+" letras.")