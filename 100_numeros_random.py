import random
i=0
tam=100
while (i<tam):
    numero=random.randint(1,100)
    i=i+1
    print("\n Numero "+str(i)+": "+str(numero))
    if (i==1):
        may=numero
        men=numero
    if (numero>may):may=numero
    if (numero<men):men=numero
print("El numero mayor es: "+str(may)+"\nEl numero menor es: "+str(men))

