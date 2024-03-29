#Función que busca el numero faltante
def missing_number(secuence, numbers):
    #En una variable se guarda la suma de la secuencia mediante la formula de la sumatoria.
    secuence_sum = secuence * (secuence + 1) // 2
    #En otra variable la suma total de los valores de la secuencia.
    list_sum = sum(numbers)
    #Devuelve la resta entre una y otra, la diferencia es el valor faltante.
    return secuence_sum - list_sum

valor = missing_number(5, [1, 2, 4, 5])
print(valor)
    
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
