import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersona:
    personas = []

    def __init__(self):
        listaDePersona = open("ficheroExterno", "ab+")
        listaDePersona.seek(0) #Volvemos el cursos al principio para lectura completa

        try: #En caso de que encuentre la lista VACIA.
            
            self.personas = pickle.load(listaDePersona) #Nos carga la lista de personas
            print("Se cargaron {} del fichero externo".format(len(self.personas)))

        except: #En caso de de ejecutar el codigo anterior, imprime condicion
            print("El ficehro esta vacio.")


    def agregarPersona(self, p):
        self.personas.append(p) #la persona P sera agregada a la lista creada

    def mostrarPersona(self):
        for p in self.personas:
            print(p)

#CREAMOS LAS PERSONAS
miLista = ListaPersona() #LLAMO 

#instancio = `p`
p=Persona("Sandra", "femenina", 34)
miLista.agregarPersona(p)

p=Persona("Antonio", "masculino", 39)
miLista.agregarPersona(p)

p=Persona("Mariela", "femenina", 30)
miLista.agregarPersona(p)

miLista.mostrarPersona()

