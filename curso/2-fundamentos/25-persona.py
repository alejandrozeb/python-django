""" Existe muchas formas de instanciar un objeto veremos  la forma mas basica"""

class Persona:
    #pass #pasara el proceso y creara una èrsona vacia
    #atributos
    def __init__(self, nombre, edad): #contructor
        self.nombre = nombre    #se crea el atributo
        self.edad = edad

#modificar los valores
Persona.nombre = "Alejandro"
Persona.edad = 85

#Acceder a los valores
print(Persona.nombre, " ", Persona.edad)
#la identacion es exactamente igual a los bloques de codigo
#python esta creando el objeto de manera implicita