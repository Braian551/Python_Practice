    # 1. Diseñar una función que calcule la media de tres números leídos del teclado y
    # poner un ejemplo de su aplicación.
suma = 0
def ciclo_num(contador, limite): #uso un  ciclo hehco con funcion para pedir los tres numeros y que se sumen
    global suma #uso global para inicializar la variable dentro de la funcion y esta no se reinicie en cada llamda de la funcion
 
    if contador <= limite: #para establecer la condicion del ciclo
        num = float(input("Ingresa un número:"))
        contador += 1
        suma += num
        
        ciclo_num(contador,limite) # se va a repetir hasta que cumpla la condicion
        prom = suma / limite
        return prom #retorno para mostrarlo porque si uso un print se va a mostrar las veces que se repite el ciclo
         
prom = ciclo_num(1,3) #lo almaceno en una variable
print("El promedio de los números ingresados es: ",prom)
