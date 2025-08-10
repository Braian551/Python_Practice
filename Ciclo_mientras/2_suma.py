print("Programa que suma y que se detiene cuando el número es cero") #informacion
num = float(input("Ingresa un número: "))#Ingreso del número
suma= 0 #inicializo la suma
while num != 0: #el ciclo se repita mientras el número sea mayor o igual que cero
   suma += num #realizo la suma y la almaceno
   print(f"Progreso de la suma {suma}")#para saber el progreso de la suma
   num = float(input("Ingresa un número: ")) #se ingresa el número

print(f"Se detiene el programa porque has ingresado {num}, y la suma total es {suma}") #Mensaje de finalización

