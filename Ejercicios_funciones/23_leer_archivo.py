# 23. Realizar un algoritmo que lea el archivo agenda e imprima los registros de toda la agenda.

def leer():
    try:
        with open("agenda.txt", "r", encoding="utf-8") as archivo:  # r = modo lectura
            contenido = archivo.read()  # lee todo el archivo
            if contenido.strip() == "":
                print("La agenda esta vacia.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("El archivo agenda.txt no existe")


leer()
