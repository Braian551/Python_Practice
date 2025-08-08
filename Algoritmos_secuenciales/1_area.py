print("1. Triángulo \n2. Rectángulo \n3. Círculo")
valor = int(input("Escoge un número para las siguientes figuras para calcular su área: "))


match valor:
    case 1:
        print("Bienvenido al Sistema de cálculo de área de Triángulo")
        bas = int(input("Ingresa la base: "))
        alt = int(input("Ingresa la altura: "))
        area = float((bas*alt)/2)
        print(f"El area del triangulo es {area}")
        
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Valor Incorrecto")
