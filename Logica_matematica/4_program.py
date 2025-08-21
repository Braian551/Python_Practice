# 4.  Un programa descarga archivos desde internet. Parte con una descarga de 6.000 MB. Descarga 450 MB por minuto y borra 150 MB de archivos temporales por minuto. 
# ¿Cuántos MB habrá descargado efectivamente después de 10 minutos? ¿cuanto espacio le quedaría si el consumo inicial  era la 4 parte de la totalidad de su capacidad? 

descarg_inical = 6000
descarga = 450
borra = 150

descarga_final = descarg_inical + (descarga * 10) - (borra * 10)
espacio = descarg_inical * 4
espacio_final = espacio - descarga_final
print(f"Los MB descargados efectivamente después de 10 minutos: {descarga_final}MB")
print(f"Espacio restante: {espacio_final}MB")