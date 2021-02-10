email = input("Introduce tu meail, por favor: ")

for i in email:
    if i =="@":
        arroba = True
        break;
    
else:
    arroba = False
    
print(arroba)