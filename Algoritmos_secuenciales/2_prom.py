#Sistema para calcular el promedio según los número que ingrese el usuario, usare el while para la cantidad de números


print("Bienvenido al sistema de cálculo para promedios")

cantidad = int(input("Cuántos números vas a ingresar: "))
contador = 1 # iniciamos con el contador desde 1 ya que la condicion la puse menor igual
resultado = 0# el resultado lo inicializo cero, ya que me va a ayudar a almacenar el numero anterior

while contador <= cantidad : #uso while para la cantidad de numeros que va a ingresar con la condicion que cuando llegue a la cantidad pare, tambien se podria haber usado for, pero quise practicar con while
    numanterior= resultado #aqui almaceno el numero anterior de cada interaccion para que no se borre o formatee
    
    nums= float(input("Ingresa un número: ")) #aqui se ingresa el número lo coloco flotante

    resultado = numanterior + nums #el resultado va en conjunto con el número anterior en la suma en el numero que se ingresa
    
   
    contador += 1 #el contador de siempre


resultadoFinal = resultado / cantidad # como el promedio es la suma de todos sus numeros divido la cantidad
print(f"El promedio de los número ingresado es {resultadoFinal}") # Y la impresión resultado 
   
