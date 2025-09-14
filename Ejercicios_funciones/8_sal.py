# 8. Escribir una función Salario que calcula los salarios de un trabajados para un
# numero dado de horas trabajadas y un salario hora. Las horas que superan las
# 40 horas semanales se pagaran como extras con un salario hora 1,5 veces el
# salario ordinario.



def sal(hora, valor_h):
    if hora <= 40:  # Si no hay horas extra
        return hora * valor_h  
    else:
        hora_n = 40  # Horas
        hora_extra = hora - 40  
        pago = hora_n * valor_h  
        extra = hora_extra * (valor_h * 1.5) 
        return pago + extra  


print(sal(45, 10000)) 
