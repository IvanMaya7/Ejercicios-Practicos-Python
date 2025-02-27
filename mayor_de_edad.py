nombre=0
anoactual=0
anonac=0
edad=0
nombre=str(input("¿Cual es su nombre? "))
anoactual=int(input("¿Cual es el ano actual? "))
anonac=int(input("¿Cual es su ano de nacimiento? "))
edad=(anoactual- anonac)
if edad >=18:
    print(nombre+ " es mayor")
else:
    print(nombre+ " es menor")
