# 9. Escribir una función booleana Digito que determine si un carácter es uno de los
# dígitos 0 al 9.


def Digito(caracter):
   
    return caracter in "0123456789" #investigando encontre que tambien in como en una matriz o vector, puede ingresar en la cadena y verificar en la funcion



print(Digito("5"))   # True
print(Digito("b"))   # False

