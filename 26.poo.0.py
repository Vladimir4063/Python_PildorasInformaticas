class Coche(): #Clase
    def __init__(self): #constructor
        self.__largoChasis = 250 #propiedades
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False  # Vehiculo detenido

    def arrancar(self, arrancamos):
        self.__enMarcha=arrancamos # encendemos el coche
        
        if(self.__enMarcha):
            chequeo = self.__chequeo_interno()
            
        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enMarcha and chequeo == False):
            return "Algo a ido mal en el chequeo. No podemos arrancar."
        
        else:
            return "El coche esta apagado"


    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno.")
        
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            
            return True
        
        else:
            
            return False
        
            
miCoche=Coche() #Instanciar una clase.
#Accedemos a las propiedades de la clase

print(miCoche.arrancar(True)) #Al llamar al metodo, la funcion cambia su valor - Arrancamos el coche  
# Antes de ver el estado del coche, lo encedimos al llamar el metodo anterior")

miCoche.estado()

#Clase/video 27

print("----------------- A continuacion creamos el segundo objeto -----------------")

miCoche2=Coche() #instanciar clase

print(miCoche2.arrancar(False))

miCoche2.estado()


