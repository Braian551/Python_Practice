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
listar_usuarios()

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
    
    
eliminar_usuario(9)
    
    
# actualizar_usuario(9, "Braian2", "braianoquen@gmail.com")
listar_usuarios()

