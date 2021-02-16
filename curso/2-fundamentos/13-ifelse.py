""" nos permite ejecutar flujos de nuestro programa cumpliendo con condiciones """

condicion = True
if condicion:
    print("La condición es verdadera")
else:
    print("La condicon es falsa")

#se cmprueba el valor de condicion verifica si es true y se va al primer bloque

""" elseif """

condicion = False
if condicion == True:
    print("La condición es verdadera")
elif condicion == False:
    print("La condicon es falsa")
else:
    print("Condición no reconocida")
    
""" Ejercicio """

numero = int(input("Proporciona un número entre 1 y 3"))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "valor fuera de rango"
    
print("numero proporcionado", numero)
""" podemos tene un bloque con solo if sin el else """

""" ternario """

print("Condicion verdadera") if condicion else print("condicion falsa")
#la primera parte es por true y la segunda por Falsa nose puede usar elseif