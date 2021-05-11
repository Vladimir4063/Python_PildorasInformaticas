import pickle

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
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", 
            self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1=Vehiculos("Honda", "RX7")
coche2=Vehiculos("FIAT", "Punto")
coche3=Vehiculos("Renault", "Megane")

coches=[coche1, coche2, coche3]
fichero=open("40.loscoches", "wb")

pickle.dump(coches, fichero) #1- nombre donde esta la coleccion. 2- donde queremos volcar la info

fichero.close()

del(fichero)

#LLAMAMOS LOS DATOS A CONSOLA

ficheroApertura=open("40.loscoches", "rb")

misCoches=pickle.load(ficheroApertura) #Vuelco la lectura binaria

ficheroApertura.close() #close arch

for c in misCoches:

    print(c.estado())

