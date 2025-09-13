# Diccionario base de talla
sizes = {
    "id": "1",
    "name": "Talla S",
    "description": "Talla pequeña para niños",
    "is_active": 1,
    "created_at": "2025-09-13 15:30:00"
}

# Crud

# Create  agregar clave y valor nuevo
sizes["extra_info"] = "Disponible en color azul"
print("Después de Create:")
for cl, vl in sizes.items():
    print(f"{cl}: {vl}")

# Read  leer valores del diccionario
print("\nNombre de la talla:", sizes["name"])
print("Estado de la talla:", "Activo" if sizes.get("is_active") else "Inactivo")

# Update  modificar varios valores
sizes.update({
    "name": "Talla M",
    "description": "Talla mediana unisex",
    "is_active": 0
})
print("\nDespués de Update:")
for cl, vl in sizes.items():
    print(f"{cl}: {vl}")

# Delete con del
del sizes["extra_info"]
print("\nDespués de Delete con del:")
for cl, vl in sizes.items():
    print(f"{cl}: {vl}")

# Delete con pop, elimina y devuelve el valor eliminado
eliminado = sizes.pop("description")
print(f"\nSe eliminó 'description', valor eliminado: {eliminado}")
print("Después de Delete con pop:")
for cl, vl in sizes.items():
    print(f"{cl}: {vl}")
