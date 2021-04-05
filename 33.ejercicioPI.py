email = input("Ingrese su correo: ")
#email = "@vladi@gmail.com"

arroba = 0
for i in email:
    if i == "@":
        arroba = arroba + 1

if i in email:
    if email[-1] == "@" or email[0] == "@" or arroba > 1 or arroba == 0 :
        print("Correo no admitido")
    else:
        print("Correo aceptado")
        