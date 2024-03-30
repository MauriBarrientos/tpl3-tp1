#Definimos la funcion para calcular la matriz espiralada. Tomamos de parametros fila y columna.
def number_spiral(fila, columna):
    #Revisa si la fila es mayor que la columna
    if fila > columna:
        #Verifica si es par o impar para calcular un patron.
        if fila % 2 == 0:
            #Si es par retorna el siguiente calculo: la fila al cuadrado menos la columna mas uno.
            return (fila**2 - columna + 1)
        else: 
            #Sino, fila menos uno, eso al cuadrado mas la columna.
            return (fila - 1) **2 + columna
    else:
        #Si la fila es menor que la columna. Primero calcula si es par o impar.
        if columna % 2 == 0:
            #Retorna: columna menos uno, al cuadrado mas la fila.
            return (columna - 1)**2 + fila
        else:
            #sino, retorna: la columna al cuadrado, menos la fila mas uno.
            return (columna**2 - fila + 1)

print(number_spiral(2, 2))
#Operador == modificado a 3 para que no de error
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"