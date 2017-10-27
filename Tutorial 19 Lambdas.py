"""Lambdas"""

#funcion regular

def suma (v1,v2):
	return v1+v2

resultado=suma(10,20)
print (resultado)

#funcion con lambda

mifuncion=lambda v1, v2 : v1+v2

resultado=mifuncion(40,50)
print (resultado)

#lambda sin valores

mifuncion=lambda:20

resultado=mifuncion()
print (resultado)

#Trabajar strings con lambdas

mifuncion= lambda sentencia: "{}?" .format(sentencia)

pregunta= mifuncion("Que es esto")
print (pregunta)