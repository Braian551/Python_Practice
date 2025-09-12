import os

def leer():
    # Definir la carpeta donde está el archivo
    carpeta = "C:/Braian/Python_Practice/Funciones"
    # Construir la ruta completa al archivo
    ruta_archivo = os.path.join(carpeta, "estudiantes_notas.txt")

    # Verificar si el archivo existe en la ruta especificada
    if os.path.exists(ruta_archivo):
        try:
            # Abrir el archivo en modo lectura con codificación utf-8
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                # Leer todo el contenido del archivo
                contenido = f.read()
            # Mostrar el contenido leído en consola
            print("contenido del archivo")
            print(contenido)
            # Retornar el contenido del archivo
            return contenido
        except Exception as e:
            # Mostrar mensaje de error si ocurre una excepción al leer el archivo
            print(f"Error al leer el archivo: {e}")
            return None
    else:
        # Mensaje si el archivo no existe en la ruta
        print("El archivo no existe")
        return None
    
leer()