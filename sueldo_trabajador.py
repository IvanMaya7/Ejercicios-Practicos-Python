sueldo=0
newsueldo=0
sueldo=int(input("¿Cual es su sueldo? "))
if sueldo>3000:
    print("No hay aumento")
else:
    newsueldo=(sueldo*0.15)
    print("su nuevo sueldo es ")
    print(newsueldo+ sueldo)
