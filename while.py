import time
import os
import sys #Libreria de manejo de sistemas de comandfo bats






#medir tiempo de for y while

# ciclo while 
inicio= time.time()
contador = 0
while contador < 10:
    print(contador)
    contador += 1
fin = time.time()

print("Tiempo transcurrido:", fin-inicio  , "segundos")



# ciclo for
inicio= time.time()
for contador in range(10):
    print(contador)
fin = time.time()

print("Tiempo transcurrido:", fin-inicio, "segundos")



if sys.platform == "win32":
    print ("el sistemas operativo win 32")
    os.system('cls')
else:
    print("el sistema operativo es otro win 64")
    os.system("clear")