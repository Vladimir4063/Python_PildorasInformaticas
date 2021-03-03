print("Recuerda: El nro no debe descender.")
num = int(input("Introduce un nro: "))

valor = True
while valor:
    nro = 0
    newNro = int(input("Ingresa un numero más elevado: "))

    if newNro < num:
        print("Ingresaste un numero menor. Saliste.")
        break;
    else:
        valor
        num = newNro

#______________________________________

nro1 = int(input("Ingresa solo nros positivos: "))
contador = 0
contador = contador + nro1
valor1 = True

while valor1:
    newNro1 = int(input("Ingresa otro nro: "))
    
    if newNro1 < 0:
        print("Ingresaste un nro negativo. Saliste.")
        print("Suma total: ", contador)
        valor1 = False
    else:
        valor1
        contador = contador + newNro1
        