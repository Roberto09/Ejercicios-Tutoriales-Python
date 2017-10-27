"""Funciones pt1"""

#Algoritmo para numero factorial

Numero=5
Factorial=1

while Numero>0:
	Factorial= Factorial*Numero
	Numero-=1
print (Factorial)


#Definir una Funcion

def factorial_numero():
	Numero=5
	Factorial=1

	while Numero>0:
		Factorial= Factorial*Numero
		Numero-=1
	print (Factorial)

factorial_numero()	

#Utilizar argumentos en una funcion

def factorial_numero(numero):
	Factorial=1

	while numero>0:
		Factorial= Factorial*numero
		numero-=1
	print (Factorial)

factorial_numero(4)
factorial_numero(5)
factorial_numero(6)

#Utilizar Return en una funcion

def factorial_numero(numero):
	Factorial=1

	while numero>0:
		Factorial= Factorial*numero
		numero-=1
	return Factorial

print (factorial_numero(10))


