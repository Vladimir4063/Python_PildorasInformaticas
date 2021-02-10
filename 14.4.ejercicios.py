
email = False

miEmail=input("Introduce tu Email verdadero: ")
arroba = 0
contador = 0

for i in miEmail:
    if (i=="@"):
        arroba = arroba + 1
    if (i=="."):
        contador = contador + 1        
if arroba == 1 and contador >= 1:
    email=True
        
if email:
    print("Email correcto.")
else:
    print("Email *Incorrecto.")


#Ejercicio 1 - Pildoras Informaticas
num = 0
for i in range(0,33):
    num = num + 3
    print(num, end=" ")

# Ejercicio 2 - Pildoras Informaticas
validar = False
pasw = input("Introduce contraseña: ")
cont = 0

espacio = 0
for i in range(len(pasw)):
    cont = cont + 1    
    if pasw[i] == " ":
        espacio = espacio + 1

if espacio == 0 and cont <= 8:
    validar = True

if validar:
    print("Contraseña OK.")
else:
    print("Contraseña érronea.")
  