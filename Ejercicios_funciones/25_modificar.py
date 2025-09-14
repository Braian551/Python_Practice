# 25. Diseñar un algoritmo que permita modificar el contenido de alguno de los
# registros del archivo secuencial agenda mediante datos introducidos por teclado.

def modificar():
    try:
        with open("agenda.txt", "r", encoding="utf-8") as archivo:
            registros = archivo.readlines()  # lee todos los registros en lista

        if not registros:
            print("La agenda esta vacia, no hay registros para modificar.")
            return

        print("Registros actuales:")
        for i, registro in enumerate(registros, start=1):
            print(f"{i}. {registro.strip()}")

        num = int(input("\nIngrese el numero de registro que desea modificar: "))

        if 1 <= num <= len(registros):
            print("\nIngrese los nuevos datos para este registro:")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            ciudad = input("Ciudad: ")
            codigo_postal = input("Código postal: ")
            telefono = input("Teléfono: ")
            edad = input("Edad: ")

            # crear el nuevo registro
            nuevo_registro = (
                f"Nombre: {nombre}, Dirección: {direccion}, Ciudad: {ciudad}, "
                f"Código postal: {codigo_postal}, Teléfono: {telefono}, Edad: {edad}\n"
            )

            # reemplazar en la lista
            registros[num - 1] = nuevo_registro

            # sobrescribir el archivo con los registros modificados
            with open("agenda.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(registros)

            print(f"\nRegistro {num} modificado correctamente.")
        else:
            print("Numero de registro invalido.")

    except FileNotFoundError:
        print("El archivo agenda.txt no existe")


modificar()
