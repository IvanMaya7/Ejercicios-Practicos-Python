precio=0
subtotal=0
total=0
for i in range (5):
    precio=int(input("inserte el valor del producto "))
    subtotal=(precio+subtotal)
    total=((subtotal* .15)+ subtotal)
print(subtotal)
print(total)
