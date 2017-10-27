"""Generadores"""

#Funcion
def generador (*args):
	"""Aqui va la documentacion de tu funcion"""
	for valor in args:
		yield valor*10

#Imprimir Documentacion

Documentacion=generador.__doc__
print(Documentacion)

#Imprimir Nombre de la fucnion

Nombre= generador.__name__
print (Nombre)

