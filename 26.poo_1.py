class Coche():
    largoChasis=250 #Propiedades de la clase
    anchoChasis=130
    ruedas=4
    enMarcha=False

    def arrancar(self): #Comportamiento de la clase "Arranca"
        self.enMarcha = True
    
    def estado(self): #Comportamiento "Informa"
        if self.enMarcha == True:
            return "El coche esta en marcha."
        else:
            return "El coche esta parado."

miCoche=Coche() #instanciar una clase

print("El largo del chasis es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, "ruedas. ")
miCoche.arrancar() #Al llamar la funcion arrancar, ya estamos cambiando el valor a True

print(miCoche.estado())