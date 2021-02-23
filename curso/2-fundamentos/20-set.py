""" Set no mantienen ningun orden ademas no se pueden agregar elementos repetidos y tampoco podemos modificar los elementos en el set, se puede eliminar """

#set es una coleccion sin orden y sin indices, no permite elementos repetidos
#y los elemtnos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
#imprime de manera desordenada
#conjunto de elemento que no tiene ningun orden

#largo
print(len(planetas))

#revisar si un elemento esta presente
print("Marte" in planetas)

#agregar nuevos elementos
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")
print(planetas)#no se agregan elementos duplicados

#eliminar con remove manda un excepción en caso no exita el elemento
planetas.remove("Tierra")
print(planetas)

#eliminar con discard no arroja excepción
planetas.discard("Jupiter")
print(planetas)
planetas.discard("Jupiter")
print(planetas)

#limpiar el set completamente
planetas.clear()
print( planetas )

#eliminar el set
del planetas