# 22.diseñar un algoritmo que permita crear un archivo Agenda de direcciones
# cuyos registros constan de los siguientes campos
# a) Nombre dirección
# b) Ciudad
# c) Código
# d) postal
# e) Teléfono
# f) edad


def guardar(archivo, n):  #  guardar registros
    if n == 0:  #  cuando ya se ingresaron todos los registros
        return
    
    print(f"\nRegistro {n}:")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    codigo_postal = input("Código postal: ")
    telefono = input("Teléfono: ")
    edad = input("Edad: ")

    # escribe todos los datos en una línea del archivo con un formato especifico
    archivo.write(
        f"Nombre: {nombre}, Dirección: {direccion}, Ciudad: {ciudad}, "
        f"Código postal: {codigo_postal}, Teléfono: {telefono}, Edad: {edad}\n"
    )

    guardar(archivo, n - 1)  # n-1 para procesar siguiente registro


def agenda():
    n = int(input("cuantos registros desea ingresar?: "))
    with open("agenda.txt", "w", encoding="utf-8") as archivo:  # w es modo de escritura, encoding para los caracteres
        guardar(archivo, n)
    print("agenda creada y guardada en agenda.txt")


agenda()  
