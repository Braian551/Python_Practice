# 13) Elimina la clave "ciudad" del diccionario persona.

persona = { "nombre": "Braian", "edad": 17, "ciudad": "medellin"}


del persona["ciudad"] # con del se elimina las claves con sus valores
print("Diccionario de persona con la clave ciudad eliminado: ", persona)