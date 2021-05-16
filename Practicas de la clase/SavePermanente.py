import pickle

class Personas:
    def __init__(self, nombre, ciudad, encuentro):
        self.nombre = nombre
        self.ciudad = ciudad
        self.encuentro = encuentro
        print("Se ha creado una persona con el nombre de ", self.nombre)