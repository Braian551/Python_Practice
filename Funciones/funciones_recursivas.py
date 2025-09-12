# funciones recursivas
n= int(input("Ingrese un numero para calcular su factorial: ")) #input para que coloque un numero entero
def factorial(n):
    return 1 if n== 0 else n * factorial(n - 1) #funcion recursiva
print(f"El factorial de {n} es: {factorial(n)}") #imprimimos el resultado

# otra forma
n == int(input("Ingrese un numero para calcular su factorial: ")) #input para que coloque un numero entero
def factorial(n, acc = 1): #acc es el acumulador
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n) #funcion recursiva con acumulador
print(factorial(n)) #imprimimos el resultado


