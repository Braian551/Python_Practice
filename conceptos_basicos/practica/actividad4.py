
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