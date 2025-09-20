import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="angelow",
        port=3306
    )

# Funciones para productos
def listar_productos():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, price FROM products WHERE is_active = 1")
    resultados = cursor.fetchall()
    
    print("\nPRODUCTOS")
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Precio: ${fila[2]}")
    
    db.close()

def insertar_producto():
    db = conectar()
    cursor = db.cursor()
    
    name = input("Nombre del producto: ")
    slug = input("Slug: ")
    description = input("Descripción: ")
    price = float(input("Precio: "))
    category_id = int(input("ID de categoría: "))
    
    sql = "INSERT INTO products (name, slug, description, price, category_id, is_active) VALUES (%s, %s, %s, %s, %s, 1)"
    valores = (name, slug, description, price, category_id)
    
    cursor.execute(sql, valores)
    db.commit()
    print("Producto insertado correctamente")
    
    db.close()

def actualizar_producto():
    db = conectar()
    cursor = db.cursor()
    
    id = int(input("ID del producto a actualizar: "))
    name = input("Nuevo nombre: ")
    price = float(input("Nuevo precio: "))
    
    cursor.execute("UPDATE products SET name=%s, price=%s WHERE id=%s", (name, price, id))
    db.commit()
    print("Producto actualizado")
    
    db.close()

def eliminar_producto():
    db = conectar()
    cursor = db.cursor()
    
    id = int(input("ID del producto a eliminar: "))
    cursor.execute("UPDATE products SET is_active=0 WHERE id=%s", (id,))
    db.commit()
    print("Producto eliminado (desactivado)")
    
    db.close()

# Funciones para usuarios
def listar_usuarios():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email, role FROM users")
    resultados = cursor.fetchall()
    
    print("\nUSUARIOS ")
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}, Rol: {fila[3]}")
    
    db.close()

def insertar_usuario():
    db = conectar()
    cursor = db.cursor()
    
    name = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    role = input("Rol (customer/admin/delivery): ")
    
    sql = "INSERT INTO users (id, name, email, password, role) VALUES (UUID(), %s, %s, %s, %s)"
    valores = (name, email, password, role)
    
    cursor.execute(sql, valores)
    db.commit()
    print("Usuario insertado correctamente")
    
    db.close()

def actualizar_usuario():
    db = conectar()
    cursor = db.cursor()
    
    id = input("ID del usuario a actualizar: ")
    name = input("Nuevo nombre: ")
    email = input("Nuevo email: ")
    
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
    db.commit()
    print("Usuario actualizado")
    
    db.close()

def eliminar_usuario():
    db = conectar()
    cursor = db.cursor()
    
    id = input("ID del usuario a eliminar: ")
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    print("Usuario eliminado")
    
    db.close()

# Funciones para tallas
def listar_tallas():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, description FROM sizes WHERE is_active = 1")
    resultados = cursor.fetchall()
    
    print("\nTALLAS")
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Descripción: {fila[2]}")
    
    db.close()

def insertar_talla():
    db = conectar()
    cursor = db.cursor()
    
    name = input("Nombre de la talla: ")
    description = input("Descripción: ")
    
    sql = "INSERT INTO sizes (name, description, is_active) VALUES (%s, %s, 1)"
    valores = (name, description)
    
    cursor.execute(sql, valores)
    db.commit()
    print("Talla insertada correctamente")
    
    db.close()

# Menú principal
def menu():
    while True:
        print("\nANGELOW")
        print("1.Productos")
        print("2.Usuarios")
        print("3.Tallas")
        print("4.Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            productos()
        elif opcion == "2":
            user()
        elif opcion == "3":
            tallas()
        elif opcion == "4":
            print("Salió correctamente")
            break
        else:
            print("Opción no válida")

def productos():
    while True:
        print("\nPRODUCTOS")
        print("1.Listar productos")
        print("2.Insertar producto")
        print("3.Actualizar producto")
        print("4.Eliminar producto")
        print("5.Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            insertar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

def user():
    while True:
        print("\nUSUARIOS ")
        print("1.Listar usuarios")
        print("2.Insertar usuario")
        print("3.Actualizar usuario")
        print("4.Eliminar usuario")
        print("5.Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            listar_usuarios()
        elif opcion == "2":
            insertar_usuario()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

def tallas():
    while True:
        print("\nTALLAS ")
        print("1.Listar tallas")
        print("2.Insertar talla")
        print("3.Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            listar_tallas()
        elif opcion == "2":
            insertar_talla()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

menu()