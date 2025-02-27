a=float(input("inserte el valor de a "))
b=float(input("inserte el valor de b "))
c=float(input("inserte el valor de c "))
d=(b*b)-(4*a*c)

if(a==0): s=("No se puede ejecutar por division de cero")
elif(d<0): s=("No se puede ejecutar por raiz negativa")
else:
        x1=(-b + d**0.5)/(2*a)
        x2=(-b - d**0.5)/(2*a)
        s="x1= "+str(x1)+"\nx2= "+str(x2)
print(s)
