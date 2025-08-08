import math as mt #añado la libreria math para traer el número pi le doy un alias por comodidad

print("1. Triángulo \n2. Rectángulo \n3. Círculo") #Un menú de guía para el usuario
valor = int(input("Escoge un número para las siguientes figuras para calcular su área: ")) #input tipo entero


match valor:
    case 1:
        print("Bienvenido al Sistema de cálculo del área del Triángulo")#Mensaje de bienvenida
        bas = float(input("Ingresa la base: "))#Los números tambien pueden ser decimales entonces los inputs tipo float
        alt = float(input("Ingresa la altura: "))
        # cálculo
        area = float((bas*alt)/2)
        print(f"El area del triangulo es {area}")
        
    case 2:
        print("Bienvenido al Sistema de cálculo del área del Rectángulo")#Mensaje de bienvenida
        bas = float(input("Ingresa la base: "))
        alt = float(input("Ingresa la altura: "))
        # cálculo
        area = float((bas*alt))
        print(f"El area del Rectángulo es {area}")
    case 3:
        print("Bienvenido al Sistema de cálculo del área del Círculo")#Mensaje de bienvenida
        rad = float(input("Ingresa el radio: "))

        # cálculo
        area = float(mt.pi * (rad ** 2)) # traigo el numero pi y lo multiplo por el radio elevado a 2
        print(f"El area del circulo es {area}")
    case _:
        print("Valor Incorrecto")# En caso de ingresar otro número
