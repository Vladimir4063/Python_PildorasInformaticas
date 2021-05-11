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
        listaDePersona = open("ficheroExterno", "wb+")
        listaDePersona.seek(0) #Volvemos el cursos al principio para lectura completa

        try: #En caso de que encuentre la lista VACIA.
            
            self.personas = pickle.load(listaDePersona) #Nos carga la lista de personas
            print("Se cargaron {} del fichero externo".format(len(self.personas)))
        #En caso de de ejecutar el codigo anterior, imprime condicion
        except: 
            print("El fichero esta vacio.")
        #Este linea se ejecutara de todas formas. Finaliza la funcion
        finally:
            listaDePersona.close() #Cerramos
            del(listaDePersona) #Eliminamos.

    def agregarPersona(self, p):
        self.personas.append(p) #la persona P sera agregada a la lista creada
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersona(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersona =open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersona) #Volcamos informacion: 1-De donde, 2-A donde.
        listaDePersona.close()
        del(listaDePersona)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas: #Recorremos la lista.
            print(p)
             
#CREAMOS LAS PERSONAS
miLista = ListaPersona() #Instancio de la clase ListaPersona

persona = Persona("Ikgvj", "mbiuno ", 24) #Instancio de la clase Persona
miLista.agregarPersona(persona) #Luego de enviar parametros, lo estamos enviando al metodo "agregarPersona" y escribimos a la lista
miLista.mostrarInfoFicheroExterno()

"""
#instancio = `p`
p=Persona("Sandra", "femenina", 34)
miLista.agregarPersona(p)

p=Persona("Antonio", "masculino", 39)
miLista.agregarPersona(p)

p=Persona("Mariela", "femenina", 30)
miLista.agregarPersona(p)

miLista.mostrarPersona()

"""