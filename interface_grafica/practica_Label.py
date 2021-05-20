from tkinter import *


root= Tk()
root.title("Primer Frame")

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

#miLabel = Label(miFrame, text="Hola Alumnos de Python", fg="red", font= ("Comic Sans MS", 18)) #damos atributos
#miLabel.place(x=200, y=200)

#miImagen=PhotoImage(file="bluePeople.gif")
#Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()