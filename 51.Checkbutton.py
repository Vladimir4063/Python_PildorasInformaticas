from tkinter import *

root=Tk()
root.title("Ejemplo")
#root.geometry("300x200")

playa = IntVar()
montania = IntVar()
sierra = IntVar()

def opcViajes():
    opcEscogida = ""

    if(playa.get() == 1):
        opcEscogida+= " Playa"
    if(montania.get() == 2):
        opcEscogida+= " Montaña"
    if(sierra.get() == 3):
        opcEscogida+= " Sierra"
    textoFinal.config(text=opcEscogida)

foto = PhotoImage(file="img/avion.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Destinos:", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcViajes).pack()
Checkbutton(frame, text="Montaña", variable=montania, onvalue=2, offvalue=0, command=opcViajes).pack()
Checkbutton(frame, text="Sierra", variable=sierra, onvalue=3, offvalue=0, command=opcViajes).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
