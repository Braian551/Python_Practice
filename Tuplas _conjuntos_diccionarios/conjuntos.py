
# creacion , las diferentes propiedades de los conjuntos, adicional
#otras operaciones.
## cracion de  los conjuntos
A={1,2,3,4,5,6,7,8,9,10}
B={2,4,6,8,10,12,14,16,18,20}# segundo conjunto
C={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

union = A.union(B)
print("Union de A y B:", union)
interseccion = A.intersection(B)
print("Interseccion de A y B:", interseccion)
diferencia = A.difference(B)
print("Diferencia de A y B:", diferencia)
# agregar valores
# agregar valores
D={1,3,5}
D.add(10)
print("conjunto D con un valor agregado:", D)

# eliminar una posicion
eliminado=A.remove(9)
print("conjunto A con un valor eliminado:", A)
# Actualizar
E = {1,2,3}
F = {4,5,6}
E.update(F)
print("Actualizacion del conjunto E:", E)
# Actualizar un solo dato
conjunto = {1, 2, 3}
conjunto.update((4,))
print(conjunto)
# simular actualizacion
conjunto = {1, 2, 3}
conjunto.update([4,5,6])
print(conjunto)

# agregar a conjunto esos valores
conjunto.remove(2)
print(conjunto)
conjunto.add(6)
# queremos que el conjunto lo recorra crea uno nuevo sin el 6
conjunto2 = conjunto.difference({6})
print(conjunto2)
# con ciclos en este caso se quitara el 4
nuevoConjunto = {x for x in conjunto if x != 4}
print(nuevoConjunto)