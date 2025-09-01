# 18) Crea una lista llamada cuadrados con los cuadrados de los números del 1 al 5 utilizando una lista por comprensión.

cuadrados = [i**2 for i in range(1,6)] # igualmente coloco la variable pero elevado al cuadrado con **2 y ya solo lo recorro con el ciclo

print("Lista de números cuadrados", cuadrados)