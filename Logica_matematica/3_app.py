# 3. Una aplicación inicia usando 2.048 MB de RAM. Por cada tarea que ejecuta, consume 180 MB más.
# Si se ejecutan 12 tareas, ¿cuánta memoria estará usando en total?. El programa debe pedir
# cuantas tareas se ejecutan.
ram_inicial = float(input("Ingrese la cantidad de RAM inicial en MB: "))

consumo_tarea = float(input("Ingrese la cantidad de RAM que consume cada tarea en MB: "))

tareas = int(input("Ingrese la cantidad de tareas que se ejecutan: "))

ram_total = ram_inicial + (consumo_tarea * tareas)
print(f"La cantidad total de RAM usada después de ejecutar {tareas} tareas es: {ram_total} MB")