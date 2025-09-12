# Funciones flecha o anónimas
# Son funciones que no tienen un nombre definido y se utilizan para operaciones simples y rápidas
# Se definen con la palabra lambda seguida de los parámetros, dos puntos y la expresión a evaluar

suma = lambda a, b: a + b  # Función flecha que suma dos números
print(suma(2, 2))  # Llamada a la función flecha y muestra el resultado

# Horas extras
horasExtras = int(input("Ingrese las horas extras trabajadas: "))  # Input para que coloque las horas extras trabajadas
calculo = lambda horasExtras: (3600 * horasExtras) * 1.25  # Función flecha para calcular horas extras diurnas
print(calculo(horasExtras))  # Llamada a la función flecha y muestra el resultado