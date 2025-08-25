# 3). Tenemos estas dos matrices A Y B: sumar

matrizA = [
    [6,1],
    [8,-2]     
           ]
matrizB = [
    [7,-2],
    [-1,4]     
           ]

matrizC = []
for f in range(2): #en rango definimos dependiendo la cantidad de filas o columnas a sumarse
    fila = []#preparamos la fila que se insertara
    for c in range(2):
        suma = matrizA[f][c] + matrizB[f][c] #y sacamos cada elemento de cada matriz y lo sumamos
        fila.append(suma)#insertamos el elemento en la fila
    matrizC.append(fila)#cuando la fila este lista ahora si lo insertamos en la matriz
    
for f in matrizC:
   print(f)
    
