import math
"""
i = 1

while i <= 10:
    print("En ejecucion " + str(i))
    i=i+1

print("Termino la ejecucion")

"""
"""
edad = int(input("Introduce tu edad por favor: "))

while edad < 5 or edad > 80:
    print("Edad incorrecta, vuelve a intentarlo.")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar, persona de", str(edad), "anios.")

"""
print("Programa decalculo de raiz cuadrada")
numero = int(input("Introduce un numero por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo.")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado.")
        break
    numero = int(input("Introduce un numero por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raíz ciadrada de " + str(numero) + " es " + str(solucion))
