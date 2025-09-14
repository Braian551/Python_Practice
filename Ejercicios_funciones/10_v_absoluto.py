# 10.Diseñar una función que permita devolver el valor absoluto de un numero.

def val_abs(n):
    # si n es mayor o igual a 0, ya es su propio valor absoluto
    if n >= 0:
        return n
    else: #sino lo volteo es decir mulplico por menos
        return val_abs(-n)

print(val_abs(5))    
print(val_abs(-8))   
