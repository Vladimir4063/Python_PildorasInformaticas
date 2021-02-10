def divide():
    try: 
        op1 = (float(input("introduce el primer numero: ")))
        op2 = (float(input("introduce el primer numero: ")))
        print("La división es: " + str(op1/op2))

    finally: #Apesar del error, se ejecuta el 'finally'
        print("Cálculo finalizado.")

divide()