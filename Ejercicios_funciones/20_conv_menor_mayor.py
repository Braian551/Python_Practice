# 20.diseñar un algoritmo de una fusión que convierta una cadena en mayúscula y
# otra que la convierta minúscula.


def mayus(cadena, i=0):  # el i contador inica en 0
    if i == len(cadena):  # cuando i llega al final, no hay más caracteres
        return ""
    char = cadena[i].upper()  # toma el caracter en posicion i y lo convierte a mayúscula
    return char + mayus(cadena, i + 1)  # concatena el caracter convertido + el resultado del resto

def minus(cadena, i=0):  # lo mismo que en mayusculas pero con lower en vez de upper
    if i == len(cadena):  
        return ""
    char = cadena[i].lower()  
    return char + minus(cadena, i + 1)  

text = "hola como estaN"  
print(mayus(text))  
print(minus(text))    