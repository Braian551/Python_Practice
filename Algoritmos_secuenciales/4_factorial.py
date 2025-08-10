#Cálculo de factorial
print("Cálculo de factorial") #mensaje de bienvenida

num = int(input("Ingresa un número: "))#Para ingresar el numero entero

factorial =1 #lo inicio en 1  par que se vaya multiplicando, porque si es con cero, siempre dara 0

for i  in range(1,num+1 ):#un ciclo for para que se multiple todos los numeros de ese fatorial, y en el rango lo inicio con 1 para que no se multiplique por cero, y le sumo 1 al numero para evitar que se quede faltando un numero
    factorial *= i #multiplico cada interaccion del for
print(factorial)#imprimo resultado