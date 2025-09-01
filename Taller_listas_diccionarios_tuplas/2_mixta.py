#2) Crea una lista llamada mixta con una cadena de texto, un número entero y un número decimal.

mixta = [] #Lo hago mas dinamico para que se inserte cada parte de la lista

texto = input("Ingresa una frase o cadena de texto: ")
mixta.append(texto)
entero = int(input("Ingresa un número entero: "))
mixta.append(entero)
decimal = float(input("Ingresa un número decimal: "))
mixta.append(decimal)

print("La lista mixta es: ", mixta)