while True :
	import random
	import time
	from time import sleep
	sleep(0.5)
	print ("\n---------------------------------------\nElige Piedra, Papel o Tijera.\nEscribelo Correctamente.")

	EComputadora= random.randint(0,2)
	EUsuario= raw_input()
	Opciones = ["Piedra", "Papel", "Tijera"]

	if (EUsuario == "Piedra") or (EUsuario == "Papel") or (EUsuario == "Tijera"):
	
		print ("\nElegiste " + EUsuario)
		print ("La Computadora Eligio " + Opciones[EComputadora])		

		if EComputadora==EUsuario:
			print ("Empataron")
		elif (EUsuario=="Piedra" and EComputadora=="Tijera") or (EUsuario=="Papel" and EComputadora=="Piedra") or (EUsuario=="Tijera" and EComputadora=="Papel"):
			print ("Ganaste")
		else:
			print ("Perdiste")
	else:
		print ("Escoge algo valido, intentalo denuevo")
