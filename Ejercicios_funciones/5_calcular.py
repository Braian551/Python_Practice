# 5. Diseñar una función que calcule X ́n para X, variable real y n variable entera.
def poten(x: float, n: int) -> float: #recibe como parametro la variable real float y luego la entera
    if n == 0: #en dado dado caso que si es cero  se devuelve 1 para evitar que se multiple por 0
        return 1
    elif n > 0:
        return x * poten(x, n - 1) #igual con el factorial se llama la funcion para simular un ciclo que se le va quitando al entero
    else:  # si n es negativo
        return 1 / poten(x, -n) #si llega a ser negativo 


print(poten(2, 3))  
print(poten(5, -2))  
print(poten(7, 0))   