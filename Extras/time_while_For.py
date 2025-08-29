import time #Captura el tiempo en segundos


#medir tiempo de for y while

# ciclo while 
inicio= time.time()#captura el tiempo inicial
contador = 0
while contador < 10:
    print(contador)
    contador += 1
fin = time.time()#capta el tiempo final

print("Tiempo transcurrido:", fin-inicio  , "segundos")#tiempo de ejecucion



# ciclo for
inicio= time.time()#captura el tiempo inicial
for contador in range(10):
    print(contador)
fin = time.time()#capta el tiempo final

print("Tiempo transcurrido:", fin-inicio, "segundos")#tiempo de ejecucion