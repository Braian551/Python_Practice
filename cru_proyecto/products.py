# Diccionario base de producto
products = {
    "id": "1",
    "name": "Camiseta Niño",
    "slug": "camiseta-nino",
    "description": "Camiseta de algodón suave para niño",
    "brand": "Angelow Kids",
    "gender": "niño",  # valores permitidos: niño, niña, bebe, unisex
    "collection": "Primavera 2025",
    "material": "Algodón 100%",
    "care_instructions": "Lavar a mano con agua fría",
    "compare_price": 50000,
    "price": 40000,
    "category_id": 2,
    "collection_id": 1,
    "is_featured": 1,
    "is_active": 1,
    "created_at": "2025-09-13 15:00:00",
    "updated_at": "2025-09-13 15:00:00"
}

# Crud

# Create  agregar clave y valor nuevo
products["stock"] = 50
print("Después de Create:")
for cl, vl in products.items():
    print(f"{cl}: {vl}")

# Read  leer valores del diccionario
print("\nNombre del producto:", products["name"])
print("Precio del producto:", products.get("price"))  # con get() evita error si no existe

# Update  modificar varios valores
products.update({
    "price": 37999,
    "is_featured": 0,
    "material": "Algodón Orgánico"
})
print("\nDespués de Update:")
for cl, vl in products.items():
    print(f"{cl}: {vl}")

# Delete con del
del products["stock"]
print("\nDespués de Delete con del:")
for cl, vl in products.items():
    print(f"{cl}: {vl}")

# Delete con pop, elimina y devuelve el valor eliminado
eliminado = products.pop("compare_price")
print(f"\nSe eliminó 'compare_price', valor eliminado: {eliminado}")
print("Después de Delete con pop:")
for cl, vl in products.items():
    print(f"{cl}: {vl}")
