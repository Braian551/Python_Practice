#5) Crea una lista llamada sublista que contenga los elementos del índice 2 al 4 de la lista números.

numeros = [] #para no hacerlo sencillo agrego cada elemento de la lista en un for
for i in range(1,11):
    numeros.append(i)

print("Lista de numeros", numeros)

sublista = numeros[2:5] #esto me indica que valores del indice o posicion voy a tomar lo dejo hasta el 5 ya que el 4 no toma el ultimo elemento

print ("La sublista con los indices del 2 al 4: ",sublista)