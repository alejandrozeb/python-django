""" es un conjuntod e elemtnos que podeoms guardar una variables"""

nombres = ['Juan', "Karla", "Ricardo" ,"Maria"] #lista de tipos string
#el indice comienza por el 0 y terminan en n-1 (0.1.2.3)
print(nombres)

#largo de la lista
print(len(nombres))

#acceder a un elemento, el primer elemento
print(nombres[0])
print(nombres[1])

#tambine podemos acceder de forma inversa con indices negativas
print(nombres[-1])

#imprimir un rango
print(nombres[0:2])
#devuelve los elemetnos 0.1

#elementos de incia hasta el indice proporcionado
print(nombres[:3])#no incluye el indice 3

#desde el indice proporcionado hasta el final
print(nombres[1:])

#cambiar los elementos de la lsita
nombres[3] = "Ivone"
print(nombres)

#iterar los elemetnos
for nombre in nombres:
    print(nombre)
    
#revisar si un elemento existe en una lista

if "Karla" in nombres:
    print("Karla si exitse en la lista")
else:
    print("El elemento buscado no existe")
    
""" arrays vs listas
    en los arrays cuando se crean o se instancia se guarda una cantidad determinado de memoria
    en listas se van creando dinamicamente
"""