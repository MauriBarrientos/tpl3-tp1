nro = (int(input("Ingresa un numero: "))) #Entrada del numero.

#Funcion que calcula la secuencia de numeros segun si es par o no.
def weird_algorithm(nro): 
    #Lista para almacenar los valores de la secuencia. Inicia con el numero ingresado.
    secuence = [nro] 
    #Bucle que se repite hasta que el numero sea 1.
    while nro != 1: 
            #Verificación de si el número es par o impar.
            if nro % 2 == 0: 
                #División por 2.
                nro //=2 
            else :
                #Operación para multiplicar por 3 y sumar 1. Esto a una variable.
                nro = nro * 3 + 1 
            #Agrega el valor de la variable a la lista.
            secuence.append(nro)
    #Retorna la lista. 
    return secuence 

#Imprime la lista
print(weird_algorithm(nro)) 

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"