# Con sep por ejemplo cambia la salida del separador de cada elemento por ejemplo una fecha
dia= 23
mes= 10
año= 2025
# sin sep
print("La fecha es: ")
print(dia, mes, año)
# con sep
print("La fecha es: ")
print(dia, mes, año, sep="/")


#con  end lo que hace es reemplazar el salto de linea por lo que le indiquemos
#con end
print("Hola", end="...")
print("Mundo")

#sin end
print("Hola")
print("Mundo")