import pickle #Library call

class Persona: #Constructor
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas = []

    #constructor de archivo
    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0) #Volvemos el cursos al principio para lectura completa

        try: #En caso de que encuentre la lista VACIA.
             
            self.personas = pickle.load(listaDePersonas) #Nos carga la lista de personas
            print("Se cargaron {} del fichero externo".format(len(self.personas)))
        #En caso de de ejecutar el codigo anterior, imprime condicion
        except: 
            print("El fichero esta vacio.")
        #Este linea se ejecutara de todas formas. Finaliza la funcion
        finally:
            listaDePersonas.close() #Cerramos
            del(listaDePersonas) #Eliminamos.

    def agregarPersonas(self, p):
        self.personas.append(p) #la persona P sera agregada a la lista creada
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas: #recorremos la lista e imprimimos
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas =open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas) #Volcamos informacion: 1-De donde, 2-A donde.
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas: #Recorremos la lista.
            print(p)
             
#CREAMOS LAS PERSONAS
miLista = ListaPersonas() #Instancio de la clase ListaPersona

persona = Persona("Adi", "Femenino ", 33) #Instancio de la clase Persona
miLista.agregarPersonas(persona) #Luego de enviar parametros, lo estamos enviando al metodo "agregarPersona" y escribimos a la lista
miLista.mostrarInfoFicheroExterno()

