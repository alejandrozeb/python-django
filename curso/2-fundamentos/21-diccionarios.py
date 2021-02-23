""" diccionarios vamos a tener dos elementos
una llava y un valor asociado a esta llave"""

#un dicconario está compuesto de llave,valor (key,value) no maneja indices si no keys

diccionario = {
    "IDE": "Integrated development Environment",
    "OPP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)

#largo
print(len(diccionario))

#acceder  a un elemento
print(diccionario["IDE"])

#otra fomra de acceder a los elementos
print(diccionario.get("IDE"))

#modificando valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario)

#Iterar, devuelve las llaves
for termino in diccionario:
    print(termino)#solo llaves
    
#iterar valores
for termino in diccionario:
    print(diccionario[termino])
    
#iterar solo valores
for valor in diccionario.values():
    print(valor)
    
#Verificar si un elemtno existe dentro de un diccionario
print("IDE" in diccionario)

#agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)
#podemos agregar cualquier tipo de datos no solo strings incluso diccioarios

#remover elementos
diccionario.pop("DBMS")
print(diccionario)

#limpiar el dicconario
diccionario.clear()
print(diccionario)
#eliminar
del diccionario

