class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")

class Camion():
    def desplazamiento(self): 
        print("Me desplazo en 6 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#Polimorfismo = Cambia su comportamiento completamente
miVehiculo = Moto()
miVehiculo = Coche()
miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo) # El parametro "miVehiculo" se almacena en "vehiculo" - line 13