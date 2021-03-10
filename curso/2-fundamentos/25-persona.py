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

#Creando un objeto
persona = Persona("Alejandro", 90)

print(persona.nombre)
print(persona.edad)
print(id(persona))#direccion de memoria

#se debe crear objetos a partir del constructor

#creacion de un segundo objeto
persona2 = Persona('Alejandro2', 25)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))#direccion de memoria

#los dos objetos se encuentran en una diferente direccion de memoria, estos objetos son independientes con sus  propios punteros