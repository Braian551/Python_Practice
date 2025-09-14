# 6) Diseñar un procedimiento que acepte un numero de mes, un numero de día y
# un numero de año y los visualice en el formato dd/mm/aa Por ejemplo, los
# valores 19,09,1987 se visualizarían así: 19/9/87 y para los valores 3,9, y 1905
# así: 3/9/05.


#hago que se envie tipo string para eliminar los ceros como en 19,09,1987, es decir eliminar el cero de 9, pasandolo a int
def fecha(dia, mes, año):
    #enteros para eliminar ceros en día y mes
    dia = int(dia)
    mes = int(mes)
    año = int(año)

    # Con modulo de 100, convierte el año de 4 cifras en dos
    año_modi = año % 100

    print(f"{dia}/{mes}/{año_modi:02d}") # 02d es un formato que hace que si es menor de dos cifras lo llena con un cero

fecha("19", "09", "1987")   
fecha("3", "9", "1905")     

