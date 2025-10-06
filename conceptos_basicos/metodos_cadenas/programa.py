nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
print("Hola, " + nombre + " " + apellido)
edad_texto = str(edad)
print("Tu edad es: " + edad_texto)

vocal= str(input("Ingrese una vocal: "))
if vocal in nombre:
    print("La vocal se encuentra en el nombre")
else:
    print("La vocal no se encuentra en el nombre")

apellido2 = str(input("Ingrese un segundo apellido: "))

if apellido2 == apellido:
    print("El primer apellido si coincide al segundo")
else:
    print("El segundo apellido no coincide con el primero")