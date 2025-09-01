# 7) Elimina el número 3 de la lista números.


numeros = [] #para no hacerlo sencillo agrego cada elemento de la lista en un for
for i in range(1,11):
    numeros.append(i)



numeros.append(11)

print("Lista de numeros", numeros)

numeros.remove(3) #con remove se elimina el valor exacto

print("Lista de numeros con el 3 eliminado: ", numeros)