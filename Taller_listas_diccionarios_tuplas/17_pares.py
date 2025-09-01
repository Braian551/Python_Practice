# 17) Crea una lista llamada numeros_pares con los números pares del 1 al 10 utilizando una lista por comprensión.

numeros_pares = [i for i in range(1,11) if i %2 == 0] # coloco la variable que se va a almacenar i, en conjunto de un ciclo, con la condicion de par


print("Lista de numeros pares", numeros_pares)