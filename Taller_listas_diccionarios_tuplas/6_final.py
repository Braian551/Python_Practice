#6) Agrega el número 11 al final de la lista números


numeros = [] #para no hacerlo sencillo agrego cada elemento de la lista en un for
for i in range(1,11):
    numeros.append(i)

print("Lista de numeros", numeros)

numeros.append(11)

print("Lista de numeros con el 11 agregado al final", numeros)