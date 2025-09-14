# 7. Realizar un procedimiento que realice la conversión de coordinadas
# polares(r,0) a coordenadas caterianas x,y
# X= r. cos(0)
# Y= r. sen(0)'


import math #uso math para los radianes y sacar coseno y seno

def polar_cart(r, th, cont=0):
    # r para radio,el  th  para el angulo en grados
    # y cont para controlar que paso hacer
    
    #convierte primero los grados a radianes 
    if cont == 0:
        return polar_cart(r, math.radians(th), cont + 1)

    #calcula coordenada x y continuar para y
    elif cont == 1:
        x = r * math.cos(th)  # x = r * coseno del ángulo
        return (x, polar_cart(r, th, cont + 1))

    #por ultimo calcula la coordenada y 
    elif cont == 2:
        return r * math.sin(th)  # y = r * seno del ángulo


print(polar_cart(5, 0))     
