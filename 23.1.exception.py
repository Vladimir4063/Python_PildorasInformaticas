import math

def calcularRaiz(num1):
    if num1<0:
        raise ValueError ("El número no puede ser negativo.")
    else:
        return math.sqrt(num1)

try:
    opc1 = int(input("Ingrese un numero: "))
    print(calcularRaiz(opc1))
except ValueError as ErrorNroNegativoOString: #Doy un alias a ese tipo de error
    print(ErrorNroNegativoOString)

print("Programa terminado.")
