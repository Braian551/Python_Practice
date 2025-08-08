import time

inicio= time.time()


contador = 0

while contador < 10:
    print(contador)
    contador += 1


fin = time.time()
print("Tiempo transcurrido")