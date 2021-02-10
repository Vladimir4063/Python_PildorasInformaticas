def GeneraPares(limite):
    
    num = 1
    
    miLista = []
    
    while num < limite:
        
        miLista.append(num*2)
        
        num = num + 1
        
    return miLista

print(GeneraPares(10))

#___________________________ Generador

def generaPares(limite1):
    
    num1 = 0
    
    while num1 < limite1:
        
        yield num1 * 2
        
        num1 = num1 + 1
        
devuelvePares=generaPares(10)

# for i in devuelvePares:
#     print (i)

print(next(devuelvePares))
print("Aca podria ir más codigo..")
print(next(devuelvePares))
print("Aca podria ir más codigo..")
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))