"""Exepciones: sirven para saber que hacer y seguir corriendo codigo despues de un error posible"""

#declarar que se debe de intentar hacer
try:
	print(2/0)
#declarar que hacer si sale mal con el tipo de error que es ya que SI LO CONOCEMOS
except ZeroDivisionError as ex:
	print (ex)
	print ("ocurrio un error pero lo conozco, dividiste entre cero")

print ("sigue el codigo")
print("\n\n\n\n")


#declarar que se debe intentar hacer
try:
	lista[1,2]
	print(lista(9))
#declarar que hacer si sale mal con un error generico ya que NO LO CONOCEMOS
except Exception as ex:
	print (ex)
	print ("ocurrio un error pero lo desconozco")


print("sigue el codigo")
print("\n\n\n\n")


#declarar que se debe intentar hacer
try:
	print(2/0)
#declarar que hacer si sale mal con un error generico ya que NO LO CONOCEMOS
except Exception as ex:
	print (ex)
	print ("ocurrio un error pero lo desconozco")
#declarar que se hara si o si aun que el programa falle
finally:
	print("se termino el script//codigo finally")