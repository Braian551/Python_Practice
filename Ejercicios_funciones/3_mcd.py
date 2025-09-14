# 3. Diseñar el algoritmo para calcular el máximo común divisor de cuatro números
# basado en una su algoritmo función mcd(el máximo común divisor de dos
# números).

a = 9
b = 45
c = 50
d = 65

# esta función calcula el máximo común divisor mcd de dos números con el algoritmo de euclides
def mcd(a, b):
    # caso base si b es cero, el mcd es a
    if b == 0:
        return abs(a) #abs para evitar que se negativo
    # se llama otra vez con (b, a % b)
    return mcd(b, a % b)

# esta función calcula el mcd de cuatro números lo hace en cadena, primero el mcd de a y b,
# luego con ese resultado calcula el mcd con c,y al final con ese resultado se calcula el mcd con d
def mcdcuatro(a, b, c, d):
    return mcd(mcd(mcd(a, b), c), d)

print(mcdcuatro(a, b, c, d))
