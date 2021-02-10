"""Simplificamos codigo quitando un 'for', utilizando 'yield from' 
"""


def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            #yield subElemento
        yield from elemento


ciudades_devueltas = devuelve_ciudades(
    "Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print("Hello")
