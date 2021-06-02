from tkinter import *
import tkinter

root = Tk()
root.geometry("250x250")

miFrame= Frame(root)
miFrame.pack()

#------------ pantalla -------------#

pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx= 10, pady=10, columnspan= 4)
pantalla.config(bg= "black", fg= "green", justify="right")

#------------ fila 1 -------------#

bt7=Button(miFrame, text= "7", width=3)
bt8=Button(miFrame, text= "8", width=3)
bt9=Button(miFrame, text= "9", width=3)
btDiv=Button(miFrame, text= "/", width=3)

bt7.grid(row=2, column=1)
bt8.grid(row=2, column=2)
bt9.grid(row=2, column=3)
btDiv.grid(row=2, column=4)

#------------ fila 2 -------------#

bt4 = Button(miFrame, text="4", width=3)
bt5 = Button(miFrame, text="5", width=3)
bt6 = Button(miFrame, text="6", width=3)
btMult = Button(miFrame, text="x", width=3)

bt4.grid(row=3, column=1)
bt5.grid(row=3, column=2)
bt6.grid(row=3, column=3)
btMult.grid(row=3, column=4)

#------------ fila 3 -------------#

bt1 = Button(miFrame, text="1", width=3)
bt2 = Button(miFrame, text="2", width=3)
bt3 = Button(miFrame, text="3", width=3)
btRest = Button(miFrame, text="-", width=3)

bt1.grid(row=4, column=1)
bt2.grid(row=4, column=2)
bt3.grid(row=4, column=3)
btRest.grid(row=4, column=4)

#------------ fila 4 -------------#

bt0 = Button(miFrame, text="0", width=3)
btComa = Button(miFrame, text=",", width=3)
btResul = Button(miFrame, text="=", width=3)
btSum = Button(miFrame, text="+", width=3)

bt0.grid(row=5, column=1)
btComa.grid(row=5, column=2)
btResul.grid(row=5, column=3)
btSum.grid(row=5, column=4)


root.mainloop()

