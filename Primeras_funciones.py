
def mensaje():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando")

# mensaje()


"""
def suma():
    num1 = 2
    num2 = 4
    print("La suma es:", num1+num2)

suma()
"""


# Funcion con parametros.
"""
def suma(num1, num2):
    print(num1+num2)


suma(5, 4)

suma(1, 2)

suma(35, 234)
"""

# Funcion con Return


def suma(num1, num2):
    resultado = num1+num2
    return resultado


print("La suma es: ", suma(5, 4))

# Guardo en una variable

almacena_resultado = (suma(5, 5))

print("2do resultado: ", almacena_resultado)
