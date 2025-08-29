# ============================================
# MANEJO DE FECHAS EN PYTHON
# ============================================
# Este script demuestra cómo trabajar con fechas y horas
# utilizando la librería datetime de Python
# ============================================

# Importación de la librería datetime
# datetime es una librería estándar de Python para manejar fechas y horas
from datetime import datetime as dt  # Importamos datetime y lo renombramos como 'dt' para facilitar su uso

# ============================================
# OBTENCIÓN DE LA FECHA Y HORA ACTUAL
# ============================================
# dt.now() devuelve un objeto datetime con la fecha y hora actual del sistema
fecha = dt.now()  # Captura la fecha y hora actual del sistema

# Mostrar la fecha y hora completa
print("Fecha actual:", fecha)  # Imprime la fecha y hora en formato completo

# ============================================
# FORMATEO DE FECHA
# ============================================
# strftime() permite formatear la fecha según especificaciones personalizadas
# %d = día del mes (01-31)
# %m = mes (01-12) 
# %Y = año con 4 dígitos (ej: 2024)
# %y = año con 2 dígitos (ej: 24)
print(fecha.strftime("%d/%m/%Y"))  # Formato: día/mes/año (ej: 25/12/2024)

# ============================================
# EJEMPLOS ADICIONALES DE FORMATO (COMENTADOS)
# ============================================
# print(fecha.strftime("%d-%m-%Y"))      # Formato: 25-12-2024
# print(fecha.strftime("%d/%m/%y"))      # Formato: 25/12/24
# print(fecha.strftime("%A %d de %B"))   # Formato: Miércoles 25 de Diciembre
# print(fecha.strftime("%H:%M:%S"))      # Formato: 14:30:45 (hora:minuto:segundo)
# print(fecha.strftime("%d/%m/%Y %H:%M")) # Formato: 25/12/2024 14:30
