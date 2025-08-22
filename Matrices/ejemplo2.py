# Identificadores: constantes y no constantes
# tipos de datos primitivos: enteros, flotantes, booleanos, cadenas de texto
# arreglos: matrices y vectores
# Las estructuras de datos es un tipo de identificador dinamico, tenemos los que son
# tipo numero, tipo cadena, tipo booleano...

# listas, tuplas, conjuntos, diccionarios, matrices...

# temas avanzados: arboles, nodos

# Creacion de una lista
lista = [1, 2, 3, 4, 5, 6, 7]  # lista de enteros
print(f"esta es la lista original: {lista}")  # mostramos la lista original
listacopia = lista
print(f"esta es la lista copia: {listacopia}")  # mostramos la lista copia

lista.append(6)  # agregamos un elemento a la lista
print(f"esta es la lista despues de agregar un elemento: {lista}")  # mostramos la lista despues de agregar un elemento
print(f"ver la posicion 4 de la lista: {lista[4]}")  # mostramos el elemento en la posicion 4 de la lista
print(f"mostrar la ultima posicion de la lista: {lista[-1]}")  # mostramos el ultimo elemento de la lista
# AGREGAR UN ELEMENTO EN UNA POSICION ESPECIFICA, un elememto 10 en la posicion 4, 
# y el valor 4 se desplaza a la posicion 5

lista.insert(4, 10)  # insertamos el elemento 10 en la posicion 4
print(f"la nueva lista es: {lista}")  # mostramos la nueva lista
# diferentes formas de eliminar valores de una lista

lista.remove(10)  # eliminamos el elemento 10 de la lista
print(f"la lista despues de eliminar el elemento 10 es: {lista}")  # mostramos la lista despues de eliminar el elemento 10
lista.pop(4)  # eliminamos el elemento en la posicion 4
print(f"la lista despues de eliminar el elemento en la posicion 4 es: {lista}")  # mostramos la lista despues de eliminar el elemento en la posicion 4
lista.pop()  # eliminamos el ultimo elemento de la lista
print(f"la lista despues de eliminar el ultimo elemento es: {lista}")  # mostramos la lista despues de eliminar el ultimo elemento
# eliminamos por indice
print(f"eliminamos el elemento en la posicion 0: {lista[0]}")  # mostramos el elemento en la posicion 0
# modificar un valor de una posicion especifica
lista[5] = 123  # modificamos el elemento en la posicion 5
print(f"la lista despues de modificar el elemento en la posicion 5 es: {lista}")  # mostramos la lista despues de modificar el elemento en la posicion 5
# cantidad de elementos de la lista
print("Cantidad de elementos de la lista",len(lista))  # mostramos la cantidad de elementos de la lista
print("Valor maximo de la lista",max(lista))  # mostramos el valor maximo de la lista
print("Valor minimo de la lista",min(lista))  # mostramos el valor minimo de la lista
print("Suma de los elementos de la lista",sum(lista))  # mostramos la suma de los elementos de la lista
lista3=[5.42,69,2,3,0,78,9]
print("ordenar la lista de menor a mayor",sorted(lista3))  # mostramos la lista ordenada de menor a mayor
# otra forma de ordenar la lista
lista3.sort()  # ordenamos la lista de menor a mayor  
lista4 = lista3  
print("ordenar la lista de menor a mayor",lista3)  # mostramos la lista ordenada de menor a mayor
# otra forma de ordenar la lista de mayor a menor
lista3.sort(reverse=True)  # ordenamos la lista de mayor a menor
print("ordenar la lista de mayor a menor",lista3)  # mostramos la lista ordenada de mayor a menor
print("la lista original no se ve afectada",lista4)  # mostramos la lista original que no se ve afectada
lista4.reverse()  # invertimos la lista
print("invertir la lista",lista4)  # mostramos la lista invertida
lista4.clear()  # limpiamos la lista
print("limpiar la lista",lista4)  # mostramos la lista limpia
# las tuplas no son mutables, no se pueden modificar despues de creadas
tupla = (4,6,0,1,4)  # creamos una tupla
print(f"esta es la tupla: {tupla}")  # mostramos la tupla
# buscar un elemento en la tupla
tupla.index(4)  # buscamos el elemento 4 en la tupla

print(f"la posicion del elemento 4 en la tupla es: {tupla.index(4)}")  # mostramos la posicion del elemento 4 en la tupla
print(f"la cantidad de veces que se repite el elemento 4 en la tupla es: {tupla.count(4)}")  # mostramos la cantidad de veces que se repite el elemento 4 en la tupla
lista5= list(tupla)  # convertimos la tupla en una lista
print(f"convertir la tupla en una lista: {lista5}")  # mostramos la lista convertida de la tupla