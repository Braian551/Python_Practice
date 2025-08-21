# 2. Una bodega inicia el día con 3.500 unidades de un producto. Cada hora ingresan 200 unidades y se despachan 300.
# ¿Cuántas unidades quedarán después de 6 horas? El programa debe pedir las cantidades de unidades iniciales.

cant_ini = int(input("Ingrese la cantidad inicial de unidades en la bodega: "))
hora_ingreso = int(input("Ingrese la cantidad de unidades que ingresan cada hora: "))
hora_despacho = int(input("Ingrese la cantidad de unidades que se despachan cada hora: "))
tiempo = int(input("Ingrese el tiempo en horas que va ha transcurrir: "))

cant_final = cant_ini + (hora_ingreso * tiempo) - (hora_despacho * tiempo)
print(f"La cantidad final de unidades en la bodega es: {cant_final}")