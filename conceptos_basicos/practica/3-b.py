num = 1
while num >= 0:
    num = int(input("Ingrese un número entero positivo o un número negativo para salir: "))
    if num == 0:
        continue
    if num > 100:
        break
    print(f"El número ingresado es: {num}")

print("ciclo terminado")