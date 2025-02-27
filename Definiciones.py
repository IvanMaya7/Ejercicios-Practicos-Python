#Definiciones
Clase=("Clase: es una entidad logica que agrupa objetos del mismo tipo")
Objeto=("Objeto: es aquel elemento que permite usar una clase, contiene datos y codigo que controla esos datos ")
Metodo=("Metodo: es un procedimiento con caracteristicas que permite darun resultado")
MetodoConstructor=("Metodo Contructor: es aquel procedimiento qu epermite inicializar las caracteristicas de una clase")
Encapsulamiento=("Encapsulamiento: Procedimiento que permite ocultar las caracteristicas de una clase")
Polimorfismo1=("Polimorfismo 1: Son metodos que tienen el mismo nombre pero reciben diferentes argumentos en la misma clase")
Polimorfismo2=("Polimorfismo 2: Son metodos con el mismo nombre, mismo numero de argumentos pero se efectua la herencia entre clases")
CaracteristicaPublica=("Caracterisitca Publica: Es una caracteristica que permite ser usada en cualquier momento desde cualquier nivel de la aplicacion")
CaracteristicaPrivada=("Caracteristica Privada: Son caracteristicas o metodos que no estan permitidos acceder a ellos por ningun motivo")
CaracteristicaProtected=("Caracteristica Protected: Permite mostrar su informacion siempre y cuando exista la herencia")

k=(str(input("Inserte \nClase \nObleto \nMetodo \nMetodo Constructor \nEncapsulamiento \nHerencia \nPolimorfismo 1 \nPolimorfismo 2 \nCaracteristicas Publica \nCaracteristica Privada \nCaracteristica Protected ")))
if (k=="Clase"):
    print(Clase)
elif (k=="Objeto"):
    print(Objeto)
elif (k=="Metodo"):
    print(Metodo)
elif (k=="MetodoConstructor"):
    print(MetodoConstructor)
elif (k=="Encapsulamiento"):
    print(Encapsulamiento)
elif (k=="Polimorfismo1"):
    print(Polimorfismo1)
elif (k=="Polimorfismo2"):
    print(Polimorfismo2)
elif (k=="CaracteristicaPublica"):
    print(CaracteristicaPublica)
elif (k=="CaracteristicaPrivada"):
    print(CaracteristicaPrivada)
elif (k=="CaracteristicaProtected"):
    print(CaracteristicaProtected)
