# tuplas solo se crean y consulta pero no se puede hacer nada mas por que es inmutable
# son inmutables es decir, no eleimi datos, no se puede agregar mas informacion
#pero permite crear listas en base de los datos que el tiene
# puedo extrar informacion de su indoice y llevarla a otra variable

tupla=(1,2,3,4,5)
print(tupla)
tuplaVacio = ()
print(tuplaVacio)
tuplaUnitaria = (1,)
print(tuplaUnitaria)

#quiero  buscar elemento y contar cuantas veces esta un valor

tupla2 = (22,2,22,3,3,4,4,5,0)
print("el numero 22 esta", tupla2.count(22), "veces")
# ·en la posicion 3 que valor hay?
print("en la posicion 3 hay", tupla2[3])

tupla3 = (0,)*5
print(tupla3)
tupla4 = ("Frase",)*5
print(tupla4)

tupla_suma = (1,2,3,4) + (5,6,7,8)
print(tupla_suma)

superTupla = sum(tupla_suma)
print(superTupla)

