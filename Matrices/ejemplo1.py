import numpy as np

# creando una matriz 2x2 =
matriz = np.array([[1, 2], [3, 4]]) #la creamos
print(matriz) # esta es la forma de mostrarla

# Creamos la maatriz para llenar las de ceros
matriz1 = np.zeros((3, 2)) # la creamos

#  f= 3 filas y c= 2 columnas
print("\033[31m", matriz1)


# otra forma de imprimir en colores
from rich import print
# Producto de matrices
matriz2 = np.array([[5, 6], [7, 8]]) 
matriz3 = np.array([[9, 10], [11, 12]])

print("[blue] el producto de la matriz [/blue]")

producto = matriz2.dot(matriz3)  # producto de matrices
print("[blue] la respuesta de la matriz es:[/blue] ",producto)  # mostramos el resultado
# la transpuesta de una matriz
transpuesta = matriz2.T  # transpuesta de la matriz
print("[purple] la transpuesta de la matriz es:[/purple] ",transpuesta)  # mostramos el resultado

# suma de matrices
suma = matriz2 + matriz3  # suma de matrices
print("[orange] la suma de las matrices es:[/orange] ",suma)  

# resta de la matriz
resta = matriz2 - matriz3  # resta de matrices
print("[red] la resta de las matrices es:[/red] ",resta)

# multiplicar por un valor escalar de una matriz 3*6
matriz4= np.array([[1,2,8,9,3,7], [3,4,5,6,7,8], [6,4,3,2,1,0]])
escalar = 2
producto_escalar = matriz4 * escalar  # multiplicación por un escalar
print("[yellow] la matriz antes del escalar es:[/yellow] \n", matriz4)  # mostramos la matriz original
print("[green] el producto escalar de la matriz es:[/green] \n",producto_escalar)  # mostramos el resultado



# otra forma de hacerlo
producto_escalar2 = np.multiply(matriz4, escalar)  # multiplicación por un escalar usando np.multiply
print("[cyan] el producto escalar de la matriz usando np.multiply es:[/cyan] \n", producto_escalar2)  # mostramos el resultado
# otra forma de hacerlo con ciclo for, recorriendo filas y columnas
# pero antes vamos a  imprimir usando ciclos

# shape nos da la forma de la matriz
# str nos da la forma de impimir otra cosa es que se convierta en texto(string)
for j in range(matriz4.shape[1]):
    columna = ""
    for i in range(matriz4.shape[0]):
        # la operacion del escalar
        columna +=str(matriz4[i,j] * escalar) + " "
    print(f"[magenta] Columna {i+j}: {columna} [/magenta]")
# diagonal superior en matrices
n=8
# matriz5= np.zeros(n,n)
diagonalSuperior = np.triu(np.ones((n, n)))
print("[orange] La diagonal superior de la matriz es: [/orange] \n", diagonalSuperior)

matriz5 = np.zeros((n, n))
print("[orange] La matriz de ceros es: [/orange] \n", matriz5)

# matriz5 que vamos a trabajar con ciclos
for f in range(n):
    for c in range(n):
        if c >= f:  # condición para la diagonal superior
            matriz5[f, c] = 1  # asignamos 1 a la posición correspondiente
print("[orange] La matriz con la diagonal superior usando ciclos es: [/orange] \n", matriz5)