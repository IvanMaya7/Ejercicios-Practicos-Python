a=float(input("inserte el valor de a "))
b=float(input("inserte el valor de b "))
c=float(input("inserte el valor de c "))
if (a==0):
    print("no se puede por valor de cero")
else:
    d=(b*b)-(4*a*c)
    if (d<0):
        print ("no se puede por raiz negativa")
    else:
        f=(d**0.5)
        x=(-b +f)
        x1=(x/(2*a))
        w=(-b -f)
        x2=(x/(2*a))
        print(str(x1)+"\n"+str(x2))
