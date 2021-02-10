
def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


print("Programa de evaluacion de notas de alumnos.")

nota1 = int(input("Ingrese nota: "))

print(evaluacion(nota1))

# Una empresa quiere premiar a los clientes mas antiguos con 10% de desc.
# Aquellos que no sean antiguos, tendran el 5%.

cliente1 = 6
cliente2 = 2


def premiar(cliente):

    premio = "Obtienes 10% desc."
    premio2 = "Obtienes 5% desc."
    if cliente >= 5:
        return premio
    return premio2


print(premiar(cliente2))

salario_presidente = int(input("Introduce salario Presidencial: "))
print("Salario presidente: " + str(salario_presidente))
