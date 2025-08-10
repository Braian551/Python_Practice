print("Programa que se detiene cuando el número es negativo") #informacion
num = float(input("Ingresa un número: "))#Ingreso del número

while num >= 0: #el ciclo se repita mientras el número sea mayor o igual que cero
   print(f"Número ingresado {num}")#para saber que número se ingreso
   num = float(input("Ingresa un número: ")) #se ingresa el número

print(f"Se detiene el programa porque has ingresado {num}") #Mensaje de finalización

