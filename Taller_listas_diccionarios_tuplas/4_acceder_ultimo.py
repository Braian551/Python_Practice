# 4) Accede al último elemento de la lista números.


numeros = [] #para no hacerlo sencillo agrego cada elemento de la lista en un for
for i in range(1,11):
    numeros.append(i)

print("Lista de numeros", numeros)
print("El último elemento es: ",numeros[-1]) #Se coloca -1, porque al colocarlo con numeros negativos se va a recorrer desde el final con -1 es como con el cero, pero a la inversa