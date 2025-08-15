import numpy as np

vector1 = np.random.randint(1, 100, 5)
print("\033[31m vector1", vector1)
vector2 = np.random.randint(1, 100, 5)
print("\033[32m vector2", vector2)
vector3 = np.random.randint(1, 100, 5)
print("\033[33m vector3", vector3)
vector4 = np.random.randint(1, 100, 5)
print("\033[34m vector4", vector4)


# Suma del vector1 y vector2
vector5 = vector1 + vector2
print("\033[35m vector1 + vector2", vector5)


#para sumar los vectores de otra forma por ciclo para

for indice in range(len(vector5)):
    vector5[indice] = vector1[indice] + vector2[indice]
print("\033[36m vector1 + vector2", vector5)


#cantidad de posiciones con len
print("\033[37m Cantidad de posiciones en vector5:", len(vector5))

# ordenar vectores 
vector5.sort()
print("\033[38m vector5 ordenado", vector5)

# sumar todos los elementos que tiene el vector3
suma = 0 
for indice in range(len(vector3)):
    suma = suma + vector3[indice]
print("\033[39m Suma de elementos en vector3:", suma)
# otra forma es 
suma= np.sum(vector3)
print("\033[39m Suma de elementos en vector3:", suma)

#  Tabla de operaciomes en vectores
suma = vector1 + vector2
resta = vector1 - vector2
multiplicacion = vector1 * vector2
division = vector1 / vector2
potencia = vector1 ** vector2
raiz = vector1 ** 0.5
print("\033[39m Tabla de operaciones en vectores:")
print("\033[39m Suma:", suma)
print("\033[39m Resta:", resta)
print("\033[39m Multiplicación:", multiplicacion)
print("\033[39m División:", division)
print("\033[39m Potencia:", potencia)
print("\033[39m Raíz:", raiz)
