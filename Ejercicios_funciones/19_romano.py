# 19.escribir un algoritmo que convierta los números arábigos en números romanos
# y viceversa I=1, V=5, X=10, L=50,C=100, D=500 y M=1000.


def convertit(num, val=None, roman=None, i=0):  
    if val is None:  #inicializa el array si es primera llamada
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  # Valores arábigos
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  # Símbolos romanos
    
    if num == 0:  # numero ya convertido 
        return ""
    
    if num >= val[i]:  # si el número es mayor o igual al valor actual
        return roman[i] + convertit(num - val[i], val, roman, i)  # usa simbol y resta valor
    else:
        return convertit(num, val, roman, i + 1)  # sino prueba el siguiente valor

print(convertit(1987)) 
print(convertit(2025))  
