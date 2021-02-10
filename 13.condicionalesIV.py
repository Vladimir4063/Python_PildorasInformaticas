# "and" = "y, si ademas" _____ Obliga a que se cumplan todas las condiciones.
# "or" = "o, sino"

# ______________________________

# distancia > 40km
# nro hermanos > 2
# salario familiar <=20.000

print("Programa de becas.")
distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el n° de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
    print("Tienes derecho a Beca.")
else:
    print("No tienes derecho a Beca.")

# __________Mismo programa, solo un cambio

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a Beca.")
else:
    print("No tienes derecho a Beca.")
