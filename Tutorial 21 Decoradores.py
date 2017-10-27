"""Deocradores en funciones"""

#Decorador basico
#A recibe a B como parametro para poder crear crear C

def decorador (func): #Funcion A Recibe (B)
	def nueva_funcion(): # Funcion C
		print("Codigo Antes")
		func()
		print ("Codigo Despues")
	return nueva_funcion

@decorador #Ejecutar la funcion de abajo con el decorador
def saluda(): #Funcion C
	print ("Hola Mundo")

saluda()

#Otra manera sin usar decoradores (@)

def decorador (func): #Funcion A Recibe (B)
	def nueva_funcion(): # Funcion C
		print("Codigo Antes")
		func()
		print ("Codigo Despues")
	return nueva_funcion() #debes agregar los parentesis en esta opcion

def saluda(): #Funcion C
	print ("Hola Mundo")

decorador(saluda)

#decorador flexible a argumentos

def decorador (func):
	def nueva_funcion(*x,**y): #Argumentos
		print ("Codigo Antes")
		func(*x,**y)
		print ("Codigo Despues")
	return nueva_funcion

@decorador
def suma(v1,v2):
	print (v1+v2)

suma(80,90)

#Lo mismo pero con returns en ves d prints

def decorador (func):
	def nueva_funcion(*x,**y):
		print ("Codigo Antes")
		resultado= func(*x,**y)
		print ("Codigo Despues")
		return resultado
	return nueva_funcion

@decorador
def suma (v1,v2):
	return (v1+v2)

x=suma(80,17)
print (x)

#Decorador con parametros

def decorador (is_valid):
	def _decorador(func):
		def before():
			print ("Codigo Antes")
		def after():
			print ("Codigo Despues")
		def nueva_funcion (*x,**y):
			if is_valid:
				before()
			resultado=func(*x,**y)
			after()
			return resultado
		return nueva_funcion
	return _decorador

@decorador (is_valid=True)
def suma (v1,v2):
	return (v1+v2)

x=suma(80,17)
print (x)

