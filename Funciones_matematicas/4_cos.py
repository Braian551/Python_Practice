import math as mt #importo la libreria math y le doy un alias mt

grad = float(input("Ingresa el grado del ángulo: ")) #input para el número tipo float

radian = mt.radians(grad)#funcion para convertirlo en radianes ya que la funcion  maneja con radianes


sin= mt.cos(radian) #aplicacion de la funcion cos
print(f"El coseno de {grad}° es aproximadamente {round(sin,2)}") #Imprimo resultado pero con round para redondearlo a 2 decimales, para evitar algo de impresición