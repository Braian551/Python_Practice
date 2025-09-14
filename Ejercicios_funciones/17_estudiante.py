# 17.dado el nombre de una serie de estudiantes y las calificaciones obtenidas en
# un examen, calcular e imprimir la calificación media así como cada calificación
# y la diferencia con la media.

def calcular(n, est, suma):  
    if n == 0: #cuando ya se ingresaron todos
        media = suma / len(est)  # calcula el promedio
        print("\ncalificacion media:", media)
        for nombre, nota in est:  # recorre lista de tuplas
            print(f"{nombre}: {nota}, diferencia con la media: {nota - media}")
        return
    nombre = input("nombre del estudiante: ")  # pide el  nombre y
    nota = float(input(f"nota de {nombre}: "))  # la nota
    est.append((nombre, nota))  # guarda  la tupla
    calcular(n - 1, est, suma + nota)  #  suma acumulada


n = int(input("¿Cuántos estudiantes hay? "))  # Cantidad de estudiantes
calcular(n, [], 0) # inicia con lista vacia y suma 0
