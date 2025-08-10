#calcular los numeros pares del uno al cien
print("Los números pares del 1 al cien son: ") #mensaje
i= 1#inicializo la variable
while i <= 100: #se va ejecutar mientra que i sea menor o igual que 100
    if i % 2 == 0: #condicion si es par con modulo
        print(i, end=", ") #imprimimos el número mas una coma y espacio en end para mejor vista, aunque en el último aparece una coma y se puede quitar con if pero mejor lo dejo asi corto
    i += 1