import random
i=0
tam=5
while (i<tam):
    numero=input("escribe un numero: ")
    i=i+1
    try:
        numero=int(numero)
    except:
        print("No es un numerito ")
        continue
    if (i==1):
        may=numero
        men=numero
    if (numero>may):may=numero
    if (numero<men):men=numero
print("El numero mayor es: "+str(may))
print("El numero menor es: "+str(men))
        
