# ============================================
# CICLOS CON BREAK Y BOOLEANOS EN PYTHON
# ============================================
# Este programa demuestra cómo usar un bucle while con True
# y la instrucción break para detener la ejecución cuando
# se cumple una condición específica
# ============================================

# Inicialización del contador
# El contador comienza en 1 y se incrementará en cada iteración
contador = 1

# ============================================
# BUCLE WHILE CON TRUE
# ============================================
# while True crea un bucle infinito que se ejecuta indefinidamente
# hasta que se encuentre una instrucción break
while True:
    # ============================================
    # CONDICIÓN DE PARADA
    # ============================================
    # Verificamos si el contador ha llegado a 10
    # Cuando se cumple esta condición, el programa se detiene
    if contador == 10:
        # Mensaje que indica que se cumplió la condición
        print(f"{contador} se cumplio la condicion y se detuvo el programa")
        # La instrucción break termina inmediatamente el bucle while
        # y continúa con el código que está después del bucle
        break
    
    # ============================================
    # CÓDIGO A EJECUTAR EN CADA ITERACIÓN
    # ============================================
    # Imprime el valor actual del contador
    print(contador)
    
    # ============================================
    # INCREMENTO DEL CONTADOR
    # ============================================
    # Incrementa el contador en 1 para la siguiente iteración
    # contador += 1 es equivalente a: contador = contador + 1
    contador += 1



