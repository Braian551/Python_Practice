import os          # Importa el módulo 'os', que permite ejecutar comandos del sistema operativo
import sys         # Importa el módulo 'sys', que permite acceder a información del sistema (como el tipo de plataforma)


# Verifica si el sistema operativo es Windows (ya sea 32 o 64 bits, siempre devuelve 'win32' en Windows)
if sys.platform == "win32":
    print("El sistema operativo es Windows")   # Muestra un mensaje indicando que el sistema es Windows
    os.system('cls')                           # Ejecuta el comando 'cls' para limpiar la pantalla en Windows
else:
    print("El sistema operativo no es Windows") # Muestra un mensaje si el sistema NO es Windows (Linux, macOS, etc.)
    os.system("clear")                          # Ejecuta el comando 'clear' para limpiar la pantalla en Linux/macOS