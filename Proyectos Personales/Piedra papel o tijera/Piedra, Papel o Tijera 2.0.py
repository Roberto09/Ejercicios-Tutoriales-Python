while True :
	import random
	import time
	from time import sleep
	sleep(0.5)
	print ("""

---------------------------------------
Elige Piedra, Papel o Tijera.
Escribelo Correctamente.""")

	EComputadora= random.randint(0,2)
	EUsuario= raw_input()
	Diccionario= {"Piedra":0, "Papel":1, "Tijera":2}
	EUsuario= Diccionario.get(EUsuario,3)
	Opciones = ["Piedra", "Papel", "Tijera"]

	if (EUsuario == 0) or (EUsuario == 1) or (EUsuario == 2):
	
		print ("\nElegiste " + Opciones[EUsuario])
		print ("La Computadora Eligio " + Opciones[EComputadora])		

		if EComputadora==EUsuario:
			print ("Empataron")
		elif (EUsuario==0 and EComputadora==2) or (EUsuario==1 and EComputadora==0) or (EUsuario==2 and EComputadora==1):
			print ("Ganaste")
		else:
			print ("Perdiste")

	else:
		print ("Escoge algo valido, intentalo denuevo")




