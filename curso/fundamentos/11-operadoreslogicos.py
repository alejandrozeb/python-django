''' nos permite compararar dos valores booleanos '''
a=3
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a<= valorMaximo) #and es operados logicos, se deben cumplir las dos para que podemos ontener un true

if(dentroRango):
    print("dentro de rango")
else:
    print("fuera de rango")
    
#el tipo de valor debe ser el mismo int con int, string con strnig

vacaciones = False
diaDescanso = False
if(vacaciones or diaDescanso):
    print("puedes ir al parque")
else:
    print("tienes deberes  que hacer")

''' por lo menos una opcion debe ser true para ingresar por ture en caso los dos sean false recien ejecuta el else  '''

 
print(not(vacaciones)) #invierte o niega el valor de la variable true a false , de false a true
