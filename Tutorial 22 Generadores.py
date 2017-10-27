"""Generadores"""

#generador con 1 valor
def generador (*args):
	for valor in args:
		yield valor*10

for x in generador(1,2,3,4,5):
	print (x)


#generador con multiples valores
def generador (*args):
	for valor in args:
		yield valor*10, valor *5

for x, y in generador(1,2,3,4,5):
	print (x,y)