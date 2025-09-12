# serie fibonacci
#numero=int(input("ingrese un numero"))
# numero=fibonacci(numero-1)+fibonacci(numero-2)
def fibonacci(numero):
  if numero==0:
    return 0
  elif numero==1:
    return 1
  else:
    return fibonacci(numero-1)+fibonacci(numero-2)
#print(fibonacci(numero))
def cicloWhile(contador,limite):
  if contador <=limite:
    #print(contador)
    print(fibonacci(contador))
    contador+=1
    cicloWhile(contador,limite)

cicloWhile(0,10)