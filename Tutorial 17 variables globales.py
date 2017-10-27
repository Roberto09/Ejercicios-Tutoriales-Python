"""Variables Globales"""
#Ejemplo 1
def polidromo (frase):
	frase=frase.replace(" ","")
	return frase==frase[::-1]

frase="anita lava la tina"

resultado=polidromo(frase)

print(resultado)

#Ejemplo 2 

def polidromo2():
	nuevo_valor= frase.replace(" ","")
	return nuevo_valor==nuevo_valor[::-1]

print(polidromo2())

#Ejemplo 3 no se pueden modificar variables globales
x=("Hola")

def polidromo3():
	x=("cambio")

print (x)
polidromo3()
print (x)

#Ejemplo cambiar variable global

def polidromo4():
	global x
	x=("cambio")

print (x)
polidromo4()
print (x)

#Ejemplo crear una variable global

def polidromo5():
	global y
	y=True

polidromo5()
print (y)


