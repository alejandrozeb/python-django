# Tupla mantine el orden, pero ya no se puede modificar
#usamos parentesis para definirlas
#una vez inicializada no podemos modig¡ficar sus valores

frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

#funciones

#largo de la tupla
print(len(frutas))

#accediendo un elemento, comienza de 0
print(frutas[1])

#navegacion inversa
print(frutas[-1])

#rangos
print(frutas[0:2]) #excluyendo el indice 2

#modificar un valor
#frutas[0] = "naranjita" #no acepta modificaciones

#modificando a lista y luego a tupla
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
print(frutas)
#modificamos con conversiones

#iterar una tupla
for fruta in frutas:
    #print(fruta)
    print(fruta, end=" ")#podemos agregar que ira como separador entre variables
    
#no podemos agregar ni eliminar elementos de la tupla

#eliminar toda la tupla
del frutas
#print(frutas)

#tambien llamada una coleccion inmutable

numeros = (13, 1, 8, 3, 2, 5, 8)
numerosLista=[]
for numero in numeros:
    if numero < 5:
        numerosLista.append(numero)
        
print(numerosLista)


 