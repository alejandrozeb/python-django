""" romper, detener  ciclos """

#imprimir solo las letra a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break #rompe todo el ciclo no entra a else
else:
    print("fin ciclo for")
    
#Imprimir pares 

for i in range(6):  #range se usa para obtener un rango 0-5
    if i % 2 != 0:
        continue    #continua con la siguiente iteracion omitiendo el resto del codigo, se va a la condicion del for
    print(i)    