#clase
class Persona():
    #atributos
    nombre= "Ivan"
    apellido="Maya Cordero"
    genero= "Masculino"
    edad= 18

    #metodos
    def hablar(self, mensaje):
        print(f' nombre: {self.nombre}')
        return mensaje

########################################

#objeto
persona = Persona()

print(persona.hablar("Hola yo soy"), "{} y mi apellido es {}, tengo {} y de genero {}".format(
    persona.nombre, persona.apellido, persona.edad, persona.genero))
