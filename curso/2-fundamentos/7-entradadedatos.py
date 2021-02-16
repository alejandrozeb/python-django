''' para que el usuario pueda ingresar datos '''

resultado = input()
print(resultado)
num1= int(input()) #convertimos la entrda en numero pero la entrada debe ser un int
num2= int(input())
print(num2)

print(num1+num2)
numero1= input()
numero2= input()
print(numero1 + numero2)#concatena los datos como string

''' para ejecutar el archivo puedes usar la consola de python y copiar el codigo,
o abrir un consola cmd o powershell y ejecutar py (nombre del archivo con la extension)
ej py 7-entradadedatos.py

y se ejecutara este archivo
'''
''' en vs podemos abrir una terminal python en la terminal '''
''' ejemplo de uso '''
print("Proporciona el titulo:")
titulo=input()
print("Proporciona el autor:")
autor=input()
print(titulo+"fue escrito por"+autor)

''' puedes agregar en input el mensaje q se recibira input ("mensaje") y se mostrara el mensaje y esperara el input'''