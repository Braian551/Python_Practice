# 16.diseñar un algoritmo que calcule el mayor valor de una lista L de N elementos

L = [5, 9, 2, 17, 4, 12]  # Lista
mayor = L[0]  
for x in L:  # recorre cada elemento hasta encontrar cada elemento
    if x > mayor: 
        mayor = x  
print("El mayor valor es:", mayor)  