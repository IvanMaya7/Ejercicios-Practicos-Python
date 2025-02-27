import random
i=0
m=5
while (i<m):
    numero=input("Inserte el numero ")
    i=i+1
    try:
        numero=int(numero)
    except:
        print("Este no es un numerito "+str(numero))
        continue
    if(i==1):
        may=numero
        men=numero
    if(numero>may): may:numero
    if(numero<men): men=numero
print()
