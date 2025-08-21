# 1. En un recipiente se depositan 35 ML de ácido A, 43 ML de ácido B y 22 ML de ácido C. Si al agitar los ácidos se evapora 
# la quinta parte del contenido total del recipiente: ¿Cuánto era el contenido inicial del recipiente? ¿Cuánto es el contenido
# que queda después de agitarse? El programa debe pedir, las cantidades de ML de acidos que se depositan en los 3 momentos. 


# voy a usar el while para pedir cantidades 


cantidad = int(input("Ingrese cuantas cantidades de ácidos se depositan en el recipiente: "))
contador = 1
total = 0
while True:
    acido = int(input(f"Ingrese la cantidad del ácido {contador} que se deposita en el recipiente: "))
    total += acido
    contador += 1
    if contador > cantidad:
        break
evapora = total / 5
total_inicial = total - evapora
print(f"El contenido inicial del recipiente era de {total} ml")
print(f"El contenido que queda después de agitarse es de {total_inicial} ml")