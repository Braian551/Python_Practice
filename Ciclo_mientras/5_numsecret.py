import random as rd #importamos esta libreria para que nos de un numero random y le añadimo un alias
print("Adivina un número del 1 al 10") #Mensaje
numsecret = rd.randint(1,10)#numero secreto del 1 al 10

num = int(input("Ingresa un número: "))#se ingresa el numero
while num != numsecret: #no se detiene hasta que sean iguales
    print("Fallastes intentanlo de nuevo")#Mensaje
    num = int(input("Ingresa un número: ")) #se ingresa el numero

print (f"Felicidades lo adivinaste el numero secreto era {numsecret}") #resultado  