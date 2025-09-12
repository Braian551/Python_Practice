# Ejemplo 2 de funcion impura
contador = 0
def incrementarContador(): #aqui se crean los parametros
    global contador #se usa la palabra global para usar la variable fuera de la funcion
    contador += 1 #aqui se realiza la operacion matematica
    return contador #aqui se devuelve el valor de la variable
print(incrementarContador()) #aqui se manda a llamar la funcion y se le pasan los parametros
print(incrementarContador()) #aqui se manda a llamar la funcion y se le pasan los parametros
print(incrementarContador()) #aqui se manda a llamar la funcion y se le pasan los parametros