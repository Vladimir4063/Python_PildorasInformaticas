class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enMarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos): #Si no heredamos de la clase "Vehiculos", daria error.
    pass


miMoto=Moto("Honda", "CBR") #Estoy pasando los parametros a la nueva clase

miMoto.estado() #Imprimo los datos atraves del atributo "estado"

miMoto.arrancar() #Terminar <-- No cambia a "True"
