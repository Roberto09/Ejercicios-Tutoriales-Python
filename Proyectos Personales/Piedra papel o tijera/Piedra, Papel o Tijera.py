import random

print ("""Elige piedra(0), papel(1) o tijera (2).
	Inserta un Numero.""")
EComputadora= random.randint(0,2)
EUsuario= int(raw_input())

Opciones = ["Piedra", "Papel", "Tijera"]

print ("Elegiste " + Opciones[EUsuario])
print ("La Computadora Eligio " + Opciones[EComputadora])

if EComputadora==EUsuario:
	print ("Empataron")
elif (EUsuario==0 and EComputadora==2) or (EUsuario==1 and EComputadora==0) or (EUsuario==2 and EComputadora==1):
	print ("Ganaste")
else:
	print ("Perdiste")
