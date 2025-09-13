# 2. Diseñar la función FACTORIAL que calcule la factorial de un número entero
# entre el rango 100 a 1.000.000.


n = int(input("Ingrese un numero para calcular su factorial: "))  # input para que coloque un numero entero

def factorial(n):
    return 1 if n== 0 else n * factorial(n - 1) #funcion recursiva

if 100 <= n <= 1000000:
    print(f"El factorial de {n} es: {factorial(n)}")
else:
    print(f"El número {n} está fuera del rango de 100 a 1,000,000")