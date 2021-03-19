class Persona ():

    def __init__(self, nombre, edad, residencia):
         
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.residencia)

#Herencia
class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        #Cree los parametros para el constructor. 
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion() #Utilizo las propiedades de Persona
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)

Antonio = Empleado(1500, 15, "Ivan", 25, "Pinamar")
#Antonio = Persona("Antonio", 55, "España") #<----- Esto si solo hereda de "Persona"

Antonio.descripcion()

print(isinstance(Antonio, Persona)) # isinstance nos permite validar si pertenece a dicha clase, devolviendo True o False

print(isinstance(Antonio, Empleado))  # seria caso False, si no estaria heredando a travez del "super" a "Persona"

