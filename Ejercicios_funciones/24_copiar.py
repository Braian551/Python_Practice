# 24. Diseñar un algoritmo que copie el archivo secuencial agenda de los ejercicios anteriores
# en un archivo directo "directo_agenda.txt", de modo que cada registro mantenga su posición relativa.

def copiar():
    try:
        with open("agenda.txt", "r", encoding="utf-8") as archivo_o:
            registros = archivo_o.readlines()  # lee todas las líneas en una lista

        with open("directo_agenda.txt", "w", encoding="utf-8") as archivo_destino:
            for registro in registros:
                archivo_destino.write(registro)  # copia cada linea igual

        print("La agenda fue copiada exitosamente a directo_agenda.txt")
    except FileNotFoundError:
        print("El archivo agenda.txt no existe")


copiar()
