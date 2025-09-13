# 3. Diseñar el algoritmo para calcular el máximo común divisor de cuatro números
# basado en una su algoritmo función mcd(el máximo común divisor de dos
# números).
a= 9
b= 45
c= 50
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def mcd_cuatro_numeros(a, b, c, d):
    return mcd(mcd(mcd(a, b), c), d)