litros=0
galones=0
costo=0
ganancia=0
litros=int(input("numero de litros"))
galones=(litros/3.785)
costo=int(input("cuanto cuesta el galon"))
ganancia=int(galones*costo)
print(ganancia)
