#Programa para saber si es par o impar 
print("Programa para saber si es par o impar ") #Mensaje de bienvenida
num = int(input("Ingresa un número:  "))# Para ingresar el número con un entero

if num % 2 == 0:  # la condicion con modulo 2 que si deja un resto es impar sino es par
    print(f"El número {num} es par")#resultado

else:
    print(f"El número {num} es impar")#resultado
 