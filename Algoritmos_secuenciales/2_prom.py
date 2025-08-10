#Sistema para calcular el promedio según los número que ingrese el usuario, usare el while para la cantidad de números


print("Bienvenido al sistema de cálculo para promedios")

cantidad = int(input("Cuántos números vas a ingresar: "))
contador = 1 # iniciamos con el contador desde 1 ya que la condicion la puse menor igual
resultado = 0# el resultado lo inicializo cero

while contador <= cantidad : #uso while para la cantidad de numeros que va a ingresar con la condicion que cuando llegue a la cantidad pare, tambien se podria haber usado for, pero quise practicar con while

    
    nums= float(input("Ingresa un número: ")) #aqui se ingresa el número, lo coloco flotante

    resultado += nums #el resultado se va sumando con cada numero que se ingrese
    
   
    contador += 1 #el contador 


resultadoFinal = resultado / cantidad # como el promedio es la suma de todos sus numeros divido la cantidad
print(f"El promedio de los número ingresado es {resultadoFinal}") # Y la impresión resultado 
   
