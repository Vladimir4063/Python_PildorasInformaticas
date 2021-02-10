miLista = ["Juan", "Guille", "Maria", "Pepe"]

miLista.append("Ivan")

miLista.insert(2, "Lulu")  # Agrego elemento en posicion

miLista.extend(["Luis", "Ana", "Lucia"])  # Agrego una lista a otra lista

print(miLista[0:3])
print(miLista[2:])

# Buscar elemento en la lista.

print("Luis" in miLista)
print("Luciana" in miLista)

# Remove

miLista.remove("Luis")
miLista.remove(1)

print(miLista)

# Eliminar ultimo elemento de la lista.

miLista.pop()
