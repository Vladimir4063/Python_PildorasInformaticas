salario_presidente=int(input("Introduce salario Presidencial: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario de Director: "))
print("Salario Director: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario de Jefe de Area: "))
print("Salario Jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario Administrativo: "))
print("Salario Administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona bien.")
else:
    print("Algo no anda bien.")