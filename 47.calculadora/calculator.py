from tkinter import *
import tkinter

root = Tk()
root.geometry("250x250")

miFrame= Frame(root)
miFrame.pack()

operacion =" "
resultado = 0
reset_pantalla = False

#-------- pulsaciones teclado ------#

numeroPantalla = StringVar()

def numeroPulsado(num):

    global operacion

    if operacion!=" ": # Si el usuario opimio +, solo mostrame por pantalla el valor"
        
        numeroPantalla.set(num) 
        operacion= " "
    
    else: # si no no oprmie +, sigue concatenando.
        numeroPantalla.set(numeroPantalla.get() + num)

#------------- resultado ---------------#

def el_resultado():
    global resultado
    global operacion

    if operacion == "suma":    
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0

#------------- sumar ---------------#

def suma(num):

    global operacion
    global resultado
    global reset_pantalla

    resultado+=int(num)
    operacion= "suma"

    reset_pantalla = True

    numeroPantalla.set(resultado)

#------------- restar ---------------#

num1 = 0
contador_resta = 0
def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else: 
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)
        
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True

#------------- multi ---------------#
contador_multi = 0
def multi(num):
    global operacion
    global resultado
    global contador_multi
    global num1
    global reset_pantalla
    """
    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1*int(num)
        else:
            resultado = int(resultado) * int(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    """

    
    resultado1 = int(num)
    operacion = "multi"
    num1 = int(numeroPantalla.get()) * resultado1 #Captura el valor de pantalla, y multi con el resul1
    resultado = num1 * resultado1
    
    numeroPantalla.set(resultado) #Envio resultado a pantalla

#------------- limpiar pantalla ---------------#
#NO TERMINADO
def limpiarPantalla():
    pantalla.delete(0, END)

def borrar():
    estado_pantalla = pantalla.get()
    if len(estado_pantalla):
        nuevoEstado_Pantala = estado_pantalla[:-1]
        limpiarPantalla()
        pantalla.insert(0, nuevoEstado_Pantala)
    else:
        limpiarPantalla()
        pantalla.insert(0, 'Error')

#------------ pantalla -------------#

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx= 10, pady=10, columnspan= 4)
pantalla.config(bg= "grey", fg= "white", justify="right")


#------------ fila 1 -------------#

btCE = Button(miFrame, text= "CE", width=3, command=lambda:limpiarPantalla())
btC = Button(miFrame, text= "C", width=3, command=lambda:borrar())
btDelete = Button(miFrame, text= "<--", width=3, command=lambda:borrar())

btCE.grid(row=2, column=1)
btC.grid(row=2, column=2)
btDelete.grid(row=2, column=3, columnspan=2, sticky=W+E)

#------------ fila 2 -------------#

bt7=Button(miFrame, text= "7", width=3, command=lambda:numeroPulsado("7"))
bt8=Button(miFrame, text= "8", width=3, command=lambda:numeroPulsado("8"))
bt9=Button(miFrame, text= "9", width=3, command=lambda:numeroPulsado("9"))
btDiv=Button(miFrame, text= "/", width=3, command=lambda:numeroPulsado("0"))

bt7.grid(row=3, column=1)
bt8.grid(row=3, column=2)
bt9.grid(row=3, column=3)
btDiv.grid(row=3, column=4)

#------------ fila 3 -------------#

bt4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
bt5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
bt6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
btMult = Button(miFrame, text="x", width=3, command=lambda:multi(numeroPantalla.get()))

bt4.grid(row=4, column=1)
bt5.grid(row=4, column=2)
bt6.grid(row=4, column=3)
btMult.grid(row=4, column=4)

#------------ fila 4 -------------#

bt1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
bt2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
bt3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
btRest = Button(miFrame, text="-", width=3, command=lambda: resta(numeroPantalla.get()))

bt1.grid(row=5, column=1)
bt2.grid(row=5, column=2)
bt3.grid(row=5, column=3)
btRest.grid(row=5, column=4)

#------------ fila 5 -------------#

bt0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
btComa = Button(miFrame, text=",", width=3, command=lambda: numeroPulsado("."))
btResul = Button(miFrame, text="=", width=3, command=lambda:el_resultado())
btSum = Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get())) # lambda llama funcion

bt0.grid(row=6, column=1)
btComa.grid(row=6, column=2)
btResul.grid(row=6, column=3)
btSum.grid(row=6, column=4)


root.mainloop()

