#Input del usuario
a = input()
#Función para hallar el palindromo
def palindrome_reorder(a):
    #Variables requeridas. Lista que ordena el string alfabeticamente.
    lista = sorted(list(set(a)))
    #Variable que almacena la mitad de la lista
    half = ""
    #Variables para almacenar un caracter impar
    odd_char = None
    #Variable para saber si hay un caracter impar
    found_odd = False

#Bucle sobre cada caracter en la cadena, "i" cuenta las veces y las almacena en "n"
    for i in lista:
        n = a.count(i)
        #Verifica si el recuento es par o no. Si lo es, agrega la mitad a "half"
        if n % 2 == 0:
            half += i * (n // 2)
        #Si es impar (y es mas de uno),activa "found_odd" e imprime "NO SOLUTION"
        elif found_odd:
            print("NO SOLUTION")
            break
        #Si solo es un caracter impar, lo almacena en "odd_char" y agrega a "half"
        else:
            found_odd = True
            odd_char = i
            half += i * (n // 2)

    #Si no hay un caracter impar, el palindromo es la mitad de la lista + la mitad invertida.
    if not found_odd:
        palindrome = half + half[::-1]
    #Si hay caracter impar, el palindromo es la mitad, mas el caracter impar y la mitad invertida.
    else:
        palindrome = half + odd_char + half[::-1]

    return palindrome

print(palindrome_reorder(a))

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"