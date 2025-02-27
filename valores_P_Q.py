p=0
q=0
total=0
p=int(input("¿cual es el valor de P? "))
q=int(input("¿cual es el valor de Q? "))
total=(((p**3* q**4) -2)*p)
if total<680:
    print(p)
    print(q)
else:
    print(input("no funciona"))
