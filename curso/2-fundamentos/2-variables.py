''' es informacion que se va a guardar en la memoria de la pc '''
x = 3
print(x)

y=3
z = x + y
print(z)
print(x)
print(y)

""" en memoria, tenemos celdas donde la primera tiene el valor de 3 otra de 5 y otra de z con punteros de referencia a los valores """

w=z
""" w tambien esta apuntando al valor de z, al literal de z, el resultado lo tenemos en un solo lugar de la memoria,
En la consola de python podemos ver la ireccion de memoria con el id(variable) y podemos verificar que el puntero de w a punto a la direccion del valor de 48
"""