# 2)Estos dibujos realizar los algoritmos que lo resuelva
from rich import print
matriz1 = [
    ["x","x","x"],
    ["x","x","x"],
    ["x","x","x"],
    ["x","x","x"],
    ["x","x","x"] ]

matriz2 = [
    ["x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x"] ]



print("Matriz 1: ") # para no documentar todo ya que es mas que todo observacion y saber que filas o columnas modificar
for f, fl1 in enumerate(matriz1): #utilizo enumarate para sacar mas facil la posicion de cada elemento, ya se en fila o columna
    for i, element in enumerate(fl1):
        if i == 0:  #ya viendo los dibujos pinto cuales si y cuales no, pero primero selecciono toda la fila o columna, y luego coloco excepto, ya sea para pintar o no 
            print(f"[blue]{element}[/]", end=" ")
        elif i == 1:  
            if f != 0 and f != 4:
                print(f"[blue]{element}[/]", end=" ")
            else:
                print(f"{element}", end=" ")
        elif i == 2:
            if f != 2:
                print(f"{element}", end=" ")
            else:
                print(f"[blue]{element}[/]", end=" ")
    print()
print()
print("Matriz 2:")
for f, fl1 in enumerate(matriz1):
    for i, element in enumerate(fl1):
        if i == 0: 
            if f != 2:
                print(f"{element}", end=" ")
            else:
                print(f"[yellow]{element}[/]", end=" ")
        elif i == 1:  
            if f != 0 and f != 4:
                print(f"[yellow]{element}[/]", end=" ")
            else:
                print(f"{element}", end=" ")
        elif i == 2:  
            print(f"[yellow]{element}[/]", end=" ")
             
        
    print()

print()
print("Matriz 3: ")
for f, fl1 in enumerate(matriz2):
    for i, element in enumerate(fl1):
        if f == 0: 
            if i == 3:
                print(f"[red]{element}[/]", end=" ")
            else:
                print(f"{element}", end=" ")
        elif f == 1:
            if i <= 1 or i >= 5:
                print(f"{element}", end=" ")

            else:
                print(f"[red]{element}[/]", end=" ")
        elif f == 2:
            if i <= 0 or i >= 6:
                print(f"{element}", end=" ")

            else:
                print(f"[red]{element}[/]", end=" ")
            
        elif f == 3:
            print(f"[red]{element}[/]", end=" ")
            
    print()


print()
print("Matriz 4: ")
for f, fl1 in enumerate(matriz2):
    for i, element in enumerate(fl1):
        if f == 3: 
            if i == 3:
                print(f"[yellow]{element}[/]", end=" ")
            else:
                print(f"{element}", end=" ")
        elif f == 2:
            if i <= 1 or i >= 5:
                print(f"{element}", end=" ")

            else:
                print(f"[yellow]{element}[/]", end=" ")
        elif f == 1:
            if i <= 0 or i >= 6:
                print(f"{element}", end=" ")

            else:
                print(f"[yellow]{element}[/]", end=" ")
            
        elif f == 0:
            print(f"[violet]{element}[/]", end=" ")
            
    print()

