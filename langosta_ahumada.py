personas=0
personas=int(input("¿Cuantas personas son?" ))
if personas<=200:
    precio=90
    presupuesto=(personas* precio)
    print ("por personas es "+ str(precio))
    print ("el total a pagar es de "+str(presupuesto))
else:
    if personas>200 and personas<=300:
        precio=85
        presupuesto=(personas* precio)
        print ("por personas es "+ str(precio))
        print ("el total a pagar es de "+str (presupuesto))
    else:
        precio=75
        presupuesto=(personas* precio)
        print ("por personas es "+ str(precio))
        print ("el total a pagar es de "+ str(presupuesto))
