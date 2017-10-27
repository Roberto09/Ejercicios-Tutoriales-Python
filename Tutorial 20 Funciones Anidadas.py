"""Funciones anidadas"""

#llamar a una funcion desde otra

def validacion (n1,n2):
	return n1>0 and n2>0

def division (n1,n2):
	if validacion(n1,n2):
		return n1/n2

resultado=division(10,2)
print (resultado)

#Funcion anidada

def division (n1,n2):
	def validacion ():
		return n1>0 and n2>0
	if validacion ():
		return n1/n2

resultado=division(2,10)
print(resultado)

#closure:funciones que crean funciones

def crear_funcion(n1,n2):
	def validacion():
		return n1>0 and n2>0
	return validacion

nueva_funcion= crear_funcion(10,9)
print (nueva_funcion())

#funcion en parametros

def crear_funcion(n1,n2):
	def validacion():
		print ("x")
		return n1>0 and n2>0
	return validacion

def aplicar_funcion(func):
	resultado=func()
	print(resultado)

nueva_funcion= crear_funcion(2,9)
print (nueva_funcion())