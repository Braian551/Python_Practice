# 18.escribir un algoritmo para contar el numero de ocurrencias de cada una de las
# palabras 'a', 'an','and' en las diferentes líneas de texto.

def contar(frases, palabras, i=0, cont=None):  
    if cont is None:  # inicializa contador si es primera llamada
        cont = {p: 0 for p in palabras}  # diccionario de palabra y contador
    if i == len(frases):  # cuando recorrio todas las líneas
        return cont
    for palabra in frases[i].lower().split():  # convierte a minusculas y separa palabras
        if palabra in cont:  # Si la palabra está en la lista buscada
            cont[palabra] += 1  # incrementa el contador
    return contar(frases, palabras, i + 1, cont)  #inicia el bucle

frases = [ 
    "a quick brown fox",
    "an apple a day",
    "and I lived happily ever after",
    "a an and a"
]

resultado = contar(frases, ['a', 'an', 'and'])  # cuenta las palabras
for p, c in resultado.items():  #recorre
    print(f"La palabra '{p}' aparece {c} veces")  
