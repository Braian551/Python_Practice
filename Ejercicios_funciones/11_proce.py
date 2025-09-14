# 11. Realizar un procedimiento que obtenga la división entera y el resto de la misma
# utilizando la únicamente los operadores suma y resta

def division_entera(dividendo, divisor, cociente=0):
    # el divisor no puede ser 0
    if divisor == 0:
        return "no puede ser cero el divisor"

    # cuando el dividendo es menor que el divisor
    if dividendo < divisor:
        return cociente, dividendo  # cociente y resto

    #Ya si cumple lo divide con recursividad
    return division_entera(dividendo - divisor, divisor, cociente + 1)


print(division_entera(17, 0))  
print(division_entera(20, 4))   
print(division_entera(4, 10))    
