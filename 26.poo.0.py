class Coche(): #Clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False #Vehiculo detenido

    def arrancar(self):
        self.enMarcha=True # encendemos el coche
    
    def estado(self):
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"


miCoche=Coche() #Instanciar una clase.

print("El largo del Chasis es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, " ruedas")
miCoche.arrancar() #Al llamar al metodo, la funcion cambia su valor - Arrancamos el coche  
print("Antes de ver el estado del coche, lo encedimos al llamar el metodo anterior")
print(miCoche.estado())