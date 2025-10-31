# 3-a

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


# 3-b
num = 1
while num >= 0:
    num = int(input("Ingrese un número entero positivo o un número negativo para salir: "))
    if num == 0:
        continue
    if num > 100:
        break
    print(f"El número ingresado es: {num}")

print("ciclo terminado")

# 3-c
nombre = input("Ingrese su nombre: ")
n = len(nombre)
print("Tu nombre {}, tiene {} caracteres".format(nombre, n))



# actividad 4
print("Bienvenido al programa de registro de usuarios.")
cantidad = 0
usuarios = {}
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre == "":
        continue
    caracteres = len(nombre)
    if caracteres <= 3:
        print("El nombre debe tener más de 3 caracteres.")
        continue
    edad = int(input("Ingrese su edad: "))
    
    usuarios[nombre] = edad
    cantidad +=1
    salida = input("Escriba 'salir' para terminar el programa o escriba cualquier palabra para continuar: ")
    if salida == "salir":
        break
    
  
print("Registro completado.")


for nombre, edad in usuarios.items():
    print("Usuario: {} - Edad: {}".format(nombre, edad), sep=" | ", end="\n")


print(F"Total de usuarios registrados: {cantidad}")