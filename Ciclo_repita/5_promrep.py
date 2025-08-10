print("Bienvenido al sitema de promedios para calificacines") #Mensaje de Bienvenida

cant = int(input("Ingresa la cantidad de notas a promediar: ")) #input para que coloque cuantas notas va ingresar, que debe ser entero
 
suma= 0 #inicializamos o creamos la variable suma que va almacenar y sumar cada nota
i= 0 #incializo el contador
while True:
    nota = float(input("Ingresa una nota: ")) #input para ingresar la nota tipo flotante
    suma += nota #se va agregando cada nota en la suma
    i +=1 #contador
    if i == cant: #condiccion para cerrar el ciclo
        break
prom= suma / cant #dividimos la suma total por la cantidad
print(f"El promedio de las notas ingresadas es {prom}") #imprimimos el resultado