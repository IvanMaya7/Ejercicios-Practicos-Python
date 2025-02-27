a=int(input("inserte el primer valor "))
b=int(input("inserte el segundo valor "))
c=int(input("inserte el tercer valor  "))
if (a>b and b>c): s=("Orden= "+str(a)+","+str(b)+","+str(c))
elif (a>c and c>b):s=("Orden= "+str(a)+","+str(c)+","+str(b))
elif (b>a and a>c):s=("Orden= "+str(b)+","+str(a)+","+str(c))
elif (b>c and c>a):s=("Orden= "+str(b)+","+str(c)+","+str(a))
elif (c>a and a>b):s=("Orden= "+str(c)+","+str(a)+","+str(b))
elif (c>b and b>a):s=("Orden= "+str(c)+","+str(b)+","+str(a))
else: s=("hay dos o tres numeros iguales")
print (s)


