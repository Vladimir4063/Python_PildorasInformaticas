"""
email = False
miEmail = input("Introduce tu email: ")

#for i in "vladimir@gmail.com":
for i in miEmail:
    if (i=="@"):
        email = True
        
if email: #deduce que debe ser True
    print("Email Correcto.")
else:
    print("Email Incorrecto.")
    
"""

contador = 0
miEmail = input("Introduce tu email: ")

#for i in "vladimir@gmail.com":
for i in miEmail:
    if (i=="@" or i=="."):
        contador = contador + 1
        
if contador == 2:
    print("Email Correcto.")
else:
    print("Email Incorrecto.")
