# funciones puras
# funciones impuras
# funciones anonimas
# funciones recursivas
# Funciones generadas
# funciones decoradas <--- es un patron de desarrollo de software
# funciones de orden superior

# Programacion funcional de leer un archivo plano


# Una funcion pura siempre devuelve el mismo resultado para las mismas entradas y no tiene efectos secundarios


# ejemplo de funciones puras sin parametro 
# para crear una funcion necesitamo sla palabra def 
# ejemplo :

def suma():  #aqui se crea la funcion
    return 2 + 2 #Return revuelve el calculo de la suma de los dos valores
print(suma()) #de esta manera mostramos en pantalla
# operar el valor de la funcion, simplemente la llevamos a una variable
valor=suma()
valor += 2
print(valor)



#ejemplo 2:


def resta():# declaramos la funcion
  total= 6-2 # realizamos la operacion matematica
  print(total) # mandamos a mostrar en pantalla
valor= resta()# en este caso la funcion apesar que es un valor matematico es tesxto, por el
# solo hecho de  usar print
tipo=type(valor)
print(tipo)# osea que la conversion no la podemos hacer
#valor=int(valor)# asi se converte el valor



# Funciones impura con parametros
a= 6
b = 8
def multplicar(a,b): #aqui se crean los parametros
    return a * b #aqui se realiza la operacion matematica

print(multplicar(a,b)) #aqui se manda a llamar la funcion y se le pasan los parametros

#Otra forma de hacerlo
print(multplicar(a,b)**2) #aqui se manda a llamar la funcion y se le pasan los parametros y se eleva al cuadrado

# Envio de parametros
horasExtras = int(input("Ingrese las horas extras trabajadas: ")) #input para que coloque las horas extras trabajadas
#Funcion de calculo de horas extras Diurnas

def calculadoraExtraDiurna(horasExtras): #aqui se crean los parametros
   return (3600*horasExtras) * 1.25 #aqui se realiza la operacion matematica
print(f"El valor a pagar por las horas extras diurnas es: {calculadoraExtraDiurna(horasExtras)}") #aqui se manda a llamar la funcion y se le pasan los parametros

