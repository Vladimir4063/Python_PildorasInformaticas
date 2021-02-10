def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    
    try:
        
        return num1 / num2 #Solo si no se ejecuta, salta a la 'exception'
    
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operacion errónea"

while True: 
    try: #Mientras cumpla esta condicion, sera True, sino sale con 'break'
        opc1 = int(input("Introduce el primer numero: "))
        opc2 = int(input("Introduce el segundo numero: "))

        break

    except ValueError:
        print("Los valores no son correctos. Inténtalo de nuevo.")


print("## suma, resta, multiplica, divide ##")
operacion=input("Introduce la operacion a realizar: ")

if operacion=="suma":
    print(suma(opc1,opc2))
    
elif operacion=="resta":
    print(resta(opc1,opc2))

elif operacion=="multiplica":
    print(multiplica(opc1,opc2))
    
elif operacion=="divide":
    print(divide(opc1, opc2))
    
else:
    print("Operación no contemplada")
    
    
print("Fin de la operación.")