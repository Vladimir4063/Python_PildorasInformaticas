import pickle

class Reunion:
    #Creamos el constructor
    def __init__(self, nombre, encuentro, ciudad):
        self.nombre = nombre
        self.encuentro = encuentro
        self.ciudad = ciudad
        print("Se ha creado una Reunión con el nombre de ", self.nombre)

    def __str__(self):
        #Damos formato para que pueda imprimirlo
        return "{} {} {}".format(self.nombre, self.encuentro, self.ciudad)

class ListaReuniones:

    reuniones = []

    #constructor de archivo
    def __init__(self):
        ListaDeReuniones = open("FicheroReuniones", "ab+")
        ListaDeReuniones.seek(0) #Volvemos al principio para hacer lectura.

        try:
            self.reuniones = pickle.load(ListaDeReuniones) #Cargamos la lista de reu.
            print("Se cargaron {} reuniones del fichero ext.".format(
                len(self.reuniones)))
        except:
            print("El fichero esta vacio.")
        finally:
            ListaDeReuniones.close() #Apesar de un fallo, el archivo va a cerrarse en memoria.
            del(ListaDeReuniones)
    
    def agregarReunion(self,p):
        self.reuniones.append(p)
        self.guardarReunionEnFicheroExt()

    def mostrarReunion(self):
        for p in self.reuniones: #Recoremos la lista e imprimimos
            print(p)

    def guardarReunionEnFicheroExt(self):
        ListaDeReuniones = open("FicheroReuniones", "wb") #Le inidicamos que sera escritura binaria = wb = write binary
        pickle.dump(self.reuniones, ListaDeReuniones) #Volcamos la lista al fichero. 1-De donde, 2-A donde.
        ListaDeReuniones.close() #Cerramos en memoria 
        del(ListaDeReuniones)

    def mostrarInfoFicheroExt(self):
        print("la informacion del fichero externo es la siguiente: ")
        for p in self.reuniones:
            print(p)

miLista = ListaReuniones() #instanciamos de la clase ListaReu..
reunion1 = Reunion("Avon", "Costos", "Toledo") #Enviamos los parametros
miLista.agregarReunion(reunion1)
miLista.mostrarInfoFicheroExt()
