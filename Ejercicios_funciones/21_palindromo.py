# 21.diseñar una función que informa si una cadena es palíndromo (una cadena es
# palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda).


def palindromo(cadena):
    # limpiar espacios y pasar a minúscula
    cadena = cadena.replace(" ", "").lower()
    
    # si la cadena tiene 0 o 1 letra, es palíndromo
    if len(cadena) <= 1:
        return "Es palindromo"
    
    # comparar primer y ultimo carácter
    if cadena[0] != cadena[-1]:
        return "No es palindromo"
    
    # Llamada la funcion  eliminando primer y último carácter
    return palindromo(cadena[1:-1])

print(palindromo("ana"))        # True
print(palindromo("hola"))       # False
