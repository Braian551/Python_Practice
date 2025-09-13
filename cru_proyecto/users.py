# Diccionario base de usuario
users = {
    "id": "1",
    "name": "Braian Andres",
    "email": "Braian@gmail.com",
    "phone": "3032242424",
    "identification_type": "cc",
    "identification_number": "323242422",
    "password": "gyhhh",
    "image": "perfil.jpg",
    "role": "customer",
    "is_blocked": 0,
    "created_at": "2025-09-13",
    "updated_at": "2025-09-13",
    "last_access": None,
    "remember_token": None,
    "token_expiry": None
}

# Crud 

# Create agregar clave y valor nuevo
users["last_name"] = "Oquendo Durango"
print("Después de Create:")
for cl, vl in users.items():
    print(f"{cl}: {vl}")

# Read leer los valores del diccionario
print("\nNombre del usuario:", users["name"])
print("Rol del usuario:", users.get("role"))  # con get() evita error si no existe

# Update modificar varios valores
users.update({
    "phone": "302424242",
    "role": "admin",
    "name": "Braian"
})
print("\nDespués de Update:")
for cl, vl in users.items():
    print(f"{cl}: {vl}")

# Delete con del
del users["last_name"]
print("\nDespués de Delete con del:")
for cl, vl in users.items():
    print(f"{cl}: {vl}")

# Delete con pop, que elimina y devuelve el valor eliminado
eliminado = users.pop("image")
print(f"\nSe eliminó 'image', valor eliminado: {eliminado}")
print("Después de Delete con pop:")
for cl, vl in users.items():
    print(f"{cl}: {vl}")
