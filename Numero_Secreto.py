import random
i=0
ns= random.randint(1,1000)
while True:
    numero= input ("Adivina el numero secreto ")
    i=i+1
    try:
        numero=int(numero)
    except:
        print("No no es un numerito")
        continue
    if(numero!=ns):
        if(numero>ns):
            print("el numero secreto es menor que "+ str(numero))
        elif(numero<ns):
            print("el numero secreto es mayor que "+ str(numero))
    else:
        print("Felicidades has encontrado el numero secreto""\n"+ str(ns)+"\nNumeros de intentos "+str(i))
        break
