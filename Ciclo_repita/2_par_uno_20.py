
i= 1 #incio la variable
suma = 0 #incio la variable
while True: #inicio el ciclo
    if i % 2 == 0:  #condicion de pares
        suma += i #sumo los numeros pares
    i+=1 #contador
    if i == 21: #condicion hasta 21 para que me sume el 20
        break #acabamos

print (f"La suma de todos lo numeros pares del 1 al 20 es {suma}") #imprimo el resultado