a=0
b=1
n=int(input("Inserte el límite: "))
while True:
    c=a+b
    a=b
    b=c
    if(c<=n):
        print(c)
    if(c>=n):
        break
