miLista = ["Juan", "Guille", "Maria", "Pepe"]

miLista2 = ["Nano", "Isabell"]

miLista3 = miLista+miLista2  # Concateno

print(miLista3)

# Ejercicio
# Agregar a Luis y Lucas en la lista de alumnos.
# Ya estan 4 de su equipo, agregarlos, luego imprimir por pantalla.

alumnos = ["Lu", "Debo", "Sol", "Norma"]

alumnos.append("Luis")  # Add

alumnos.extend(["Luis", "Lucas"])

print(alumnos)
