import math as mt #importo la libreria math y le doy un alias mt

bas = float(input("Ingresa la base: ")) #input para el número tipo float
exp = float(input("Ingresa el exponente: ")) #input para el número tipo float



pot= mt.pow(bas,exp) #aplicacion de la funcion pow para potencias
print(f"{bas} elevedo a {exp} da como resultado {pot}") #Imprimo resultado