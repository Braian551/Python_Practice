# 12.Escribir una función que permita deducir si una fecha leída del teclado es
# válida.


def fecha_v(dia, mes, año):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # dias por mes 
    
    # verifica mes entre 1-12 Y dia entre 1 y máximo días del mes
    if 1 <= mes <= 12 and 1 <= dia <= dias_mes[mes - 1]:# dias_mes[mes-1] porque el array empieza en 0 pero los meses en 1
        return True
    return False


def fecha():
    dia = int(input("Dia: "))  
    mes = int(input("Mes: "))  
    año = int(input("Año: "))  

    if fecha_v(dia, mes, año):  # Si la fecha es valida
        print(f"fecha: {dia}/{mes}/{año}")  # Muestra la fecha
        return dia, mes, año  # retorna los valores
    else:
        print("fecha invalida")
        return fecha() 
        

fecha()
