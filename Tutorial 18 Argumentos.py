"""Argumentos (en funciones)"""
#Argumentos regulares

def suma (v1, v2):
	return v1+v2

resultado= suma(10,8)
print (resultado)

#Argumentos con valor asignado

def suma (v1,v2):
	print (v1+v2)

resultado=suma(v2=30,v1=10)

#Multiples argumentos sin valor sin saber cuantos

def suma(*argumentos):
	print (argumentos)

resultado= suma(10,20,30) #Esto me imprimira una tupla

def suma(*caca28):
	x=0
	for valores in caca28:
		x=x+valores
	return x

result=suma(10,20,30)
print (result)

#Multiples argumentos con valor sin saber cuantos
"""
def suma(**argumentos):
	return argumentos

result= suma(hola="eduardo", x=5)
print (result)

"""
def suma(**argumentos):
	valor= argumentos.get("x",2)
	return (valor)

resultado= suma (hola="eduardo", y=5)
print (resultado)