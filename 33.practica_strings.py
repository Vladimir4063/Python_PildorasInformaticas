nombre = input("Ingresa tu nombre: ")

print("Tu nombres es ", nombre.upper()) #Mayúscula

print("Tu nombres es ", nombre.lower()) #Minúscula

print("Tu nombres es ", nombre.capitalize()) #primera letra en Mayús.

edad = input("Introduce edad: ")
#print(edad.isdigit()) #devuelve True si es un entero

while(edad.isdigit()==False):
    print("Por favor, introduce un numero")

    edad = input("Introduce edad: ")
    
if (int(edad) < 18):
    print("No puede pasar")
else:
    print("Puede pasar.")
