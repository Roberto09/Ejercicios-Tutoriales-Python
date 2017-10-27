#Funciones Basicas

#Metodo Return
def Suma (v1, v2):
	return v1+v2

print Suma(2,8)

#Metodo llamar funcion
def Multiplicacion (v1,v2):
	print (v1*v2)

Multiplicacion(2,9)

#Funciones con parametros

def Multiplicacion (v1,v2=10): #Esto quiere decir que si no se le asigna un valor a v2 la accion se ejecutara asignandole el valor dado en los parametros.
	return v1*v2

print Multiplicacion(2)

#Asignar argumentos con sus variables

def Multiplicacion (v1,v2=10): 
	return v1*v2

print Multiplicacion(v2=10, v1=30)

#Return Multiples Valores en una Funciones

#Metodo 1
def Multiples():
	return "String",1,True,2.83

print Multiples()[0]

#Metodo 2

def Multiples():
	return "String",1,True,2.83

string, entero, booleano, flotante=Multiples()

print (booleano)

#Diferentes funciones dentro de otras

def variables (funcion):
	print funcion(6,8)

variables (Multiplicacion)













