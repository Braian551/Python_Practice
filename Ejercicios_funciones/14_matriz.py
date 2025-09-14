# 14.rellenar una matriz identidad de 4x 4


def matriz(n):  
    # 1 en diagonal (i==j), 0 en resto
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

for fila in matriz(4):  # recorre las filas
    print(fila)  