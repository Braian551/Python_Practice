suma = 0 #inicializamos la variable

for i in range(1,21):#comenzamos desde el 1 hasta el 21, para que coja el 20, tambien se puede iniciar desde el 2
   
    if i %2 == 0: #la condicion si es par
        suma += i #sumamos en cada interacción
print(f"La suma de los numeros pares del 1 al 20 es {suma}") #imprimo el resultado