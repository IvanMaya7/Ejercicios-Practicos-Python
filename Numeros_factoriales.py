#num=int(input("Inserte un número: "))
#m=num
#s=str(num)
#while(m>1):
   # m=m-1
  #  num=num*m
 #   s=s+" X "+str(m)
#print("Factorial: "+str(s)+"= "+str(num))

def calcular_fac(numero):
    if numero==0 or numero==1:
        return 1
    else: return numero*calcular_fac(numero-1)
ingreso=int(input("Inserte un número: "))
resultado=calcular_fac(ingreso)
print(f"el factorial de {ingreso} es {resultado}")
