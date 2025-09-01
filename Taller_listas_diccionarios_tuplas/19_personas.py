# Crea un diccionario llamado personas con los nombres y edades de varias personas.
# Luego, crea una lista llamada mayores con los nombres de las personas mayores de 
# edad (mayores o iguales a 18 años).

personas = {"persona1":{
    "nombre": "Braian", "edad":17  
},
"persona2":{
    "nombre": "Maria", "edad":16
},
"persona3":{
    "nombre": "Rodrigo", "edad":25  
},
"persona4":{
    "nombre": "Alejandro", "edad":10  
},
"persona5":{
    "nombre": "Marolyn", "edad":18  
},        } #Creo dentro del dicionario claves como persona, pero estas claves teniedo como valor otro diccionario con
# la informacion de cada uno, con su valor y clave

mayores = [] #creo la lista

for clave, valor in personas.items(): #saco todo de personas con sus claves y valores
    # y lo separo en dos variables, clave que seria la clave principal y valor 
    # representa digamos ese diccionaroc con sus valores y claves, con el for recorro cada clave
    if valor["edad"] >= 18: # y saco la clave edad, en si su valor con la condicion
        mayores.append(valor["nombre"]) #ya agrego el valor de nombre
print("Personas mayor de edad:", mayores)

