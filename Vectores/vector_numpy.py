import numpy as np
#este es la abreviatura de numpy para mejor manejo "np"
# creacion de un vector con 5 posiciones
vector = np.zeros(5)
print("\033[31m el vector de ceros", vector)
# vector per con unos
vector1= np.ones(5)
print("\033[32m el vector de unos", vector1)
# crear un vector con valorea aleatorios de un arango del 1 al 100 5 posiciones
vector2= np.random.randint(1,100,5) #con enteros
print("\033[34m el vector de numeros aleatorios", vector2)

vector3= np.random.rand(5)
print("\033[35m el vector de numeros aleatorios decimales", vector3)


# Crearlo con ceros y con un ciclo llenarlo

numero= np.zeros(5)
print("\033[36m numeros para llenarlo manualmente", numero)
# asi se recorre para mostrarlo por medio de un for
for interante in vector2:
    print("numero" , interante)

# cambiar los valores del vector con datos de introduccion por teclado
for indice in range(len(numero)) :
  numero[indice]=float(input("ingrese el numero: "))
print("\033[32m numeros para llenarlo manual: \n", numero)
