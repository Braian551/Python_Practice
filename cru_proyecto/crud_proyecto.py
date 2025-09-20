# Diccionarios de la base del proyecto
producto = {
    "id": "1",
    "name": "Camiseta Niño",
    "slug": "camiseta-nino",  
    "description": "Camiseta de algodón suave para niño",
    "brand": "Angelow Kids",
    "gender": "niño",
    "collection": "Primavera 2025",
    "material": "Algodón 100%",
    "care_instructions": "Lavar a mano con agua fría",
    "compare_price": 50000,  # Precio original para mostrar descuento
    "price": 40000,
    "category_id": 2,  # Referencia a tabla categorías
    "collection_id": 1,  # Referencia a tabla colecciones
    "is_featured": 1,  # 1=destacado, 0=normal
    "is_active": 1,  # 1=activo, 0=inactivo
    "created_at": "2025-09-13 15:00:00",
    "updated_at": "2025-09-13 15:00:00"
}

tallas = {
    "id": "1",
    "name": "Talla S",
    "description": "Talla pequeña para niños",
    "is_active": 1,  # 1=disponible, 0=no disponible
    "created_at": "2025-09-13 15:30:00"
}

user = {
    "id": "1",
    "name": "Braian Andres",
    "email": "Braian@gmail.com",
    "phone": "3032242424",
    "identification_type": "cc",  # cc, ti, pasaporte, etc.
    "identification_number": "323242422",
    "password": "gyhhh",  
    "image": "perfil.jpg",
    "role": "customer",  
    "is_blocked": 0,  # 1=bloqueado, 0=activo
    "created_at": "2025-09-13",
    "updated_at": "2025-09-13",
    "last_access": None,  # Timestamp del último login
    "remember_token": None,  # Para mantener sesión
    "token_expiry": None  # Cuándo expira el token
}

# Funciones CRUD básicas
def crear(diccionario, clave, valor):
    diccionario[clave] = valor
    print(f"Se agrego '{clave}': {valor}")

def leer_elemento(diccionario, clave):
    if clave in diccionario:
        return diccionario[clave]
    else:
        return f"La clave '{clave}' no existe en el diccionario"

def actualizar(diccionario, clave, valor):
    if clave in diccionario:
        diccionario[clave] = valor
        print(f"Se actualizó '{clave}': {valor}")
    else:
        print(f"La clave '{clave}' no existe en el diccionario")

def eliminar(diccionario, clave):
    if clave in diccionario:
        valor_eliminado = diccionario.pop(clave)  # .pop() elimina y retorna el valor
        print(f"Se eliminó '{clave}': {valor_eliminado}")
    else:
        print(f"La clave '{clave}' no existe en el diccionario")

def mostrar(diccionario, nombre):
    print(f"\n{nombre} completo:")
    for clave, valor in diccionario.items():  # .items() devuelve pares clave-valor
        print(f"{clave}: {valor}")

# Menus de cada diccionario
def menu_product():
    global producto  # Acceso global a la variable producto
    while True:
        print("\nMENÚ DE PRODUCTO")
        print("1.Agrega una nueva clave-valor")
        print("2.Consulta el valor por clave")
        print("3.Actualiza un valor existente")
        print("4.Elimina una clave-valor")
        print("5.Mostrar producto completo")
        print("6.Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clave = input("Ingrese la nueva clave: ")
            valor = input("Ingrese el valor: ")
            crear(producto, clave, valor)
            
        elif opcion == "2":
            clave = input("Ingrese la clave a consultar: ")
            resultado = leer_elemento(producto, clave)
            print(f"Valor de '{clave}': {resultado}")
            
        elif opcion == "3":
            clave = input("Ingrese la clave a actualizar: ")
            if clave in producto:  # Validación antes de actualizar
                valor = input("Ingrese el nuevo valor: ")
                actualizar(producto, clave, valor)
            else:
                print(f"La clave '{clave}' no existe")
                
        elif opcion == "4":
            clave = input("Ingrese la clave a eliminar: ")
            eliminar(producto, clave)
            
        elif opcion == "5":
            mostrar(producto, "Producto")
            
        elif opcion == "6":
            break  # Sale del bucle while
            
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_t():
    global tallas
    while True:
        print("\nMENÚ DE TALLAS")
        print("1.Agrega una nueva clave-valor")
        print("2.Consulta el valor por clave")
        print("3.Actualiza un valor existente")
        print("4.Elimina una clave-valor")
        print("5.Mostrar talla completo")
        print("6.Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clave = input("Ingrese la nueva clave: ")
            valor = input("Ingrese el valor: ")
            crear(tallas, clave, valor)
            
        elif opcion == "2":
            clave = input("Ingrese la clave a consultar: ")
            resultado = leer_elemento(tallas, clave)
            print(f"Valor de '{clave}': {resultado}")
            
        elif opcion == "3":
            clave = input("Ingrese la clave a actualizar: ")
            if clave in tallas:
                valor = input("Ingrese el nuevo valor: ")
                actualizar(tallas, clave, valor)
            else:
                print(f"La clave '{clave}' no existe")
                
        elif opcion == "4":
            clave = input("Ingrese la clave a eliminar: ")
            eliminar(tallas, clave)
            
        elif opcion == "5":
            mostrar(tallas, "Tallas")
            
        elif opcion == "6":
            break
            
        else:
            print("Opción no válida, intente nuevamente.")

def menu_user():
    global user
    while True:
        print("\nMENÚ DE USUARIO: ")
        print("1.Agrega una nueva clave-valor")
        print("2.Consulta el valor por clave")
        print("3.Actualiza un valor existente")
        print("4.Elimina una clave-valor")
        print("5.Mostrar usuario completo")
        print("6.Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clave = input("Ingrese la nueva clave: ")
            valor = input("Ingrese el valor: ")
            crear(user, clave, valor)
            
        elif opcion == "2":
            clave = input("Ingrese la clave a consultar: ")
            resultado = leer_elemento(user, clave)
            print(f"Valor de '{clave}': {resultado}")
            
        elif opcion == "3":
            clave = input("Ingrese la clave a actualizar: ")
            if clave in user:
                valor = input("Ingrese el nuevo valor: ")
                actualizar(user, clave, valor)
            else:
                print(f"La clave '{clave}' no existe")
                
        elif opcion == "4":
            clave = input("Ingrese la clave a eliminar: ")
            eliminar(user, clave)
            
        elif opcion == "5":
            mostrar(user, "Usuarios")
            
        elif opcion == "6":
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

# Menú principal
def menu():
    while True:
        print("\nSISTEMA DE CRUD: ")
        print("1.Gestionar Productos")
        print("2.Gestionar Tallas")
        print("3.Gestionar Usuarios")
        print("4.Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_product()
        elif opcion == "2":
            menu_t()
        elif opcion == "3":
            menu_user()
        elif opcion == "4":
            print("Salio del crud")
            break  # Termina 
        else:
            print("Opción no válida, intente nuevamente")

menu()  