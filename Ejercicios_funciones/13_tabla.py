# 13.escribir el algoritmo que permita obtener el número de elementos positivos de
# una tabla.


def cont_pos(tabla, indice=0): 
    #si ya recorrimos toda la tabla
    if indice == len(tabla):  #cuando llegamos al final del array
        return 0  #no hay más elementos, retorna 0

    #si el elemento actual es positivo, sumamos 1
    if tabla[indice] > 0:  #verifica si el número en posición indice es positivo
        return 1 + cont_pos(tabla, indice + 1)  #suma 1 + resultado del resto de la tabla
    else:
        return cont_pos(tabla, indice + 1)  # no suma nada, solo continua con el siguiente



num = [3, -1, 7, 0, -5, 8, 2]  
print("cantidad de positivos:", cont_pos(num))   
