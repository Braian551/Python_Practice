# 1). Realizar una matriz de 5*5 y llenarlo con los siguientes datos:
# 25 12 26 7 15
# 12 12 2 9 25
# 25 6 4 25 6
# 1 4 6 10 9
# 2 25 8 5 8
# 
# *Debe sumar todos los números ingresados.
# *Cuando la matriz este llena, deben contar de cada número cuantos hay repetidos y llenar
# un vector con esa información imprimiéndolo en pantalla, ejemplo: el número 25 se
# repite 5 veces.
from rich import print
# para hacerlo mas dinamico se hara introduciendo los numeros manualmente en la matriz
filas = 5 #defino las filas que tendra para pasarselo al for
columnas = 5 #igualmente con las columnas
matriz = [] #aqui se almcenara las filas con sus columnas

for i in range(filas): #hacemos que el ciclo for nos inicie cada fila
    fila = []# para almacenar las filas que sera introducidas en la matriz, cuando el cilo se repite obviamente la fila queda otra vez vacia
    for m in range(columnas): #ahora en cada columna de una fila se introducira un elemento
        elemento = int(input(f"Ingrese el valor de la fila [{i}] de la columna [{m}]: ")) #guardamos el elemento
        fila.append(elemento) #añadimos los elementos en su fila
    matriz.append(fila) #despues de tener todos los elementos añadimos la fila a la matriz



#ya teniedo la matriz siguen las operaciones
suma = 0
count = {} #con un diccionario servira mas facil contar cada elemento y almacenar       
for n in matriz: #imprimimos cada fila de la matriz
    for element in n: #y sacamos cada elemento
        suma += element #cada elemento se sumara
        if element in count: #si dentro de count se encuentra con ese elemento, le sumara uno mas a su valor con su respectiva clave
            count[element] +=1 
        else:
            count[element] = 1#en caso de que no este que es obvio que al principio, entonces creara la clave con su valor igual a 1
            
print("[blue]La matriz es: [/]") 
#imprimos la matriz con la misma secuencia anterior
for fil in matriz:
    for elem in fil:
        print(f"[yellow]{elem}[/]", end=" ") #pero no queremos todos los elementos hacia abajo
        #entonces cada elemento se imprimira en una linea con end para simular una fila
    print()#ya cuando termine la primera fila ahora si un salto de linea

print(f"[green]La suma de todos sus valores es: {suma}[/]")

contador = 0 #ahora para contar si hay numeros repetidos
for dic in count.values(): #sacamos solos los valores de las claves, que se almacenan en dic
    if dic >= 2: #si hay uno mayor o igual que dos el contador sumara
        contador +=1
    
    
if contador > 0:    #y la condicion para eso
    print(f"[violet]Numeros repetidos: {contador}[/]") 
else:
    print("[red]no hay numeros repetidos[/]")   

repetidos = [] #aqui almaceno el vector como indica el punto
for num, cant in count.items():#y saco cada clave y valor, en forma de tupla, y en el num y cant, almacento tanto su clave y valor
    if cant >= 2:# si hay uno que sea igual a 2 o supere lo añado al vector, y lo muestro en el print
        repetidos.append(num)
        print(f"[blue]el número {num} se repite {cant} veces. [/]")
if contador >=2: 
    print(f"[red]El vector con los numeros repetidos:\n{repetidos}[/]")

        

        
