# 4. Diseñar una función que encuentro el mayor de dos números enteros.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

def encontrarmayor(num1, num2):
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    else:
        print(f"El número {num2} es mayor que {num1}")

encontrarmayor(num1, num2)