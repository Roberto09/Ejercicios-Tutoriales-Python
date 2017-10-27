"""Argv para "llamar" funciones sin siquiera abrir el programa"""
#importar la libreria sys
import sys
#imprimir los argumentos (el nombre es un argumento que siempre esta incluido.)
print (sys.argv)

#hacer algo de acuerdo al parametro dado con if statements

if len(sys.argv)==1:
	print("inserta un argumento despues del nombre")
elif len(sys.argv)>1:
	print(sys.argv[1])


#correr alguna funcion de acuerdo al argumento
#declaracion de funciones prueba:

def suma(n1,n2):
	print(n1+n2)

def resta(n1,n2):
	print(n1-n2)

def multiplicacion(n1,n2):
	print(n1*n2)

#comprovar que tengas un segundo argumento minimo
if len(sys.argv)>1:
	argUsuario=sys.argv[1]
	#revisar que escogio el usuario y de acuerdo a eso ejecutar alguna funcion.
	if argUsuario == "suma":
		print("Escogiste suma, debes escoger 2 numeros a sumasr")
		n1= input("numero 1: ")
		n2= input("numero 2: ")
		suma(n1,n2)

	if argUsuario == "resta":
		print("Escogiste resta, debes escoger 2 numeros a sumasr")
		n1= input("numero 1: ")
		n2= input("numero 2: ")
		resta(n1,n2)

	if argUsuario == "multiplicacion":
		print("Escogiste multiplicacion, debes escoger 2 numeros a sumasr")
		n1= input("numero 1: ")
		n2= input("numero 2: ")
		multiplicacion(n1,n2)
#mensaje de error
else:
	print("inserta un argv")