# 15.calcular la suma de los elementos de la diagonal principal de una matriz de 4x4

def suma_diag(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Suma diagonal principal:", suma_diag(matriz))  
