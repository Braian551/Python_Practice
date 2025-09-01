# 16) Crea una lista llamada pares con todos los pares clave-valor del diccionario persona.

persona = { "nombre": "Braian", "edad": 17, "ciudad": "medellin"}

pares = list(persona.items()) #con list lo transformamos en una lista, y con items() traemos todos los pares clave valor del diccionario, aunque cada par en tupla



print("Pares clave-valor del diccionario persona: ", pares)