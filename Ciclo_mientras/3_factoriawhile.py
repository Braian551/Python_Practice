print("Sitema para calcular el factorial de un número") #Mensaje sobre el programa

num = int(input("Ingresa un número: ")) #el numero a calcular
i= 1 #inicializo la variable
fact = 1 #inicializo la variable
while num >= i : #el codigo se va ejecutar mientras el numero sea mayor o igual que i, sino se detiene
    fact *= i #vamos multplicando cada numero hasta que i llegue al numero ingresado, ya que asi es el calculo del factrial que es la multplicacion de todos sus números anteriores
    i +=1 # contado
print(f"El factorial de {num} es {fact}") #imprimos el resultado