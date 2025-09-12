#  simular un ciclo
# limite valor de parada
# contador

def ciclo(contador):
  if contador>0:
    print(contador)
    contador-=1
    ciclo(contador-1)
ciclo(10)
print("fin del ciclo")
# otra forma 1 al 10
def cicloWhile(contador,limite):
  if contador <=limite:
    print(contador)
    contador+=1
    cicloWhile(contador,limite)
cicloWhile(1,10)

print("fin del ciclo")
# 
def preguntaSicontinua(inicial):
    print(inicial)
  
    respuesta=input("desea continuar? s/n: ")
    if respuesta.lower() == "s" and inicial<10:
        print("Vamos en el puesto", inicial)
     
        preguntaSicontinua(inicial+1)

    else:
        print("fin del ciclo")
preguntaSicontinua(0)