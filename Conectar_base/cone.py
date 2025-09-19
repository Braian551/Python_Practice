import mysql.connector

def conectar():
    return mysql.connector.connect(
     host = "localhost",
     user = "root",
     password ="root",
     database = "ejemplo",
     port = 3306   
        
        
    )
    
db=conectar()
cursor=db.cursor()
db.commit()
db.close()
print("Verificar si la conexion esta bien hecha")

def listar_usuarios():
    db= conectar()
    cursor = db.cursor()
    resultados = cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    
    db.close()
    
    
    
def insertar_usuario(nombre, email):  # Agregar parámetros
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO usuarios(nombre, email) VALUES(%s, %s)"
    valores = (nombre, email)
    cursor.execute(sql, valores)
    db.commit()
    cursor.close()  # Buen práctica: cerrar cursor
    db.close()
    print("Usuario insertado correctamente")

# insertar_usuario("Braian", "braianoquen@gmail.com")
# listar_usuarios()

def actualizar_usuario(id,nombre,email):
    db=conectar()
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET nombre=%s, email= %s WHERE id=%s;",(nombre,email,id))
    db.commit()
    cursor.close()
  
    db.close()
    print("actualizado")

def eliminar_usuario(id):
    db=conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s",(id,))
    db.commit()
    print("eliminado el id: ", id)
    db.close
    
    
# eliminar_usuario(9)
    
    
# actualizar_usuario(9, "Braian2", "braianoquen@gmail.com")
# listar_usuarios()

def menu():
    while True:
        print("Bienvenido al sistema de base de datos elija su opcion")
        print("1 Insertar usuarios")
        print("2 es actualizar usuarios")
        print("3 es eliminar usuarios")
        print("4 es listar usuarios")
        print("5 es salir")
        opcion= int(input("Ingresa un número"))
        match opcion:
            case 1:
                nombre = input("ingrese su nombre")
                email = input("ingrese su email")
                insertar_usuario(nombre,email)
            case 2:
                id = int(input("Ingrese el id: "))
                nombre = input("ingrese su nombre")
                email = input("ingrese su email")
                actualizar_usuario(id,nombre, email)
            case 3:
                id = int(input("Inserta el id: "))
                eliminar_usuario(id)
            case 4:
                listar_usuarios()
            case 5:
                print("Has salido del sistema")
                break;
            case __:
                print("no coloco opcion correcta")
menu()
        