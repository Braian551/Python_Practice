# va a verificar si la cadena "Hola mundo" termina con la subcadena "mundo"

texto = "Hola mundo"
#con true
resultado = texto.endswith("mundo")
print(resultado)  
#con false
resultado = texto.endswith("Hola")
print(resultado)  
