import random
import time
"""Declaracion variables y algoritmos en general"""
#Algoritmo 2 valores horizontal
dvph={}
for w,x in enumerate(range(1,37)):
	if x%6==0:
		pass
	else:
		y=x+1
		dvph[w]=[x,y]


#Algoritmo 2 valores vertical
dvpv={}
for w,x in enumerate(range(1,37)):
	if x>30:
		pass
	else:
		y=x+6
		dvpv[w]=[x,y]


#Algoritmo 3 valores horizontal
tvph={}
for w,x in enumerate(range(1,37)):
	if x%6==0 or (x+1)%6==0:
		pass
	else:
		y=x+1
		z=y+1
		tvph[w]=[x,y,z]


#Algoritmo 3 valores vertical
tvpv={}
for w,x in enumerate(range(1,37)):
	if x>24:
		pass
	else:
		y=x+6
		z=y+6
		tvpv[w]=[x,y,z]
"""Declaracion variables y algoritmos en general"""




"""Eleccion Usuario"""

#Eleccion barco de largo 2
c1=True
while c1:
	time.sleep(0.5)
	print ("Elige la posicion de tu barco con un largo de 2 puntos")
	EUsuarioP1B2= input("la primera posicion es: ")
	EUsuarioP2B2= input("la segunda posicion es: ")

	EusuarioB2= [EUsuarioP1B2,EUsuarioP2B2]

	if EusuarioB2 in dvph.values() or EusuarioB2 in dvpv.values():
		time.sleep(0.5)
		print ("\ntu barco esta posicionado sobre " + str(EusuarioB2))
		c1=False
	else:
		print ("Intentalo denuevo por favor \n \n --------------------------------")

print ("Tu barco ah sido registrado")


#Eleccion barco de largo 3
c2=True
while c2:
	time.sleep(0.5)
	print ("--------------------------------------------\nElige la posicion de tu barco con un largo de 3 puntos")
	EUsuarioP1B3= input("la primera posicion es: ")
	EUsuarioP2B3= input("la segunda posicion es: ")
	EUsuarioP3B3= input("la tercera posicion es: ")

	EusuarioB3= [EUsuarioP1B3,EUsuarioP2B3,EUsuarioP3B3]

	if EusuarioB3 in tvph.values() or EusuarioB3 in tvpv.values():
		time.sleep(0.5)
		print ("\ntu barco esta posicionado sobre " + str(EusuarioB3))
		c2=False
	else:
		print ("Intentalo denuevo por favor \n \n --------------------------------")

print ("Tu barco ah sido registrado")

time.sleep(0.5)
print("\n----------------------------------------------------\nLa posiciones de tus barcos son "+str(EusuarioB2)+"y "+str(EusuarioB3))	

"""Eleccion Usuario"""



"""Eleccion de Computadora"""
dvertical_u_horizontal=random.randint(0,1)
tvertical_u_horizontal=random.randint(0,1)

#Algoritmos 2 valores horizontales
def Advph():
	global EComputadora2

	EComputadora2= random.randint(0,len(dvph))

	EComputadora2= dvph[EComputadora2]
	print (EComputadora2)

def Advpv():
	global EComputadora2

	EComputadora2= random.randint(0,len(dvpv))

	EComputadora2= dvpv[EComputadora2]
	print (EComputadora2)

#Algoritmos 2 valores verticales
def Atvph():
	global EComputadora3

	EComputadora3= random.randint(0,len(tvph))

	EComputadora3= tvph[EComputadora3]
	print (EComputadora3)

def Atvpv():
	global EComputadora3

	EComputadora3= random.randint(0,len(tvpv))

	EComputadora3= tvpv[EComputadora3]
	print (EComputadora3)



dlista=[Advph,Advpv]
tlista=[Atvph,Atvpv]

d=dlista[dvertical_u_horizontal]
d()
t=tlista[tvertical_u_horizontal]
t()
time.sleep(1)
print ("La computadora ya hizo su eleccion")
"""Eleccion Computadora"""



"""Algoritmo de juego"""

juego=True

while juego:

	if EusuarioB2==0 and EusuarioB3==0:
		juego=False
		time.sleep(0.5)
		print ("Lo siento soldado, nos han ganado")
	elif EComputadora2==0 and EComputadora3==0:
		juego=False
		time.sleep(0.5)
		print("En hora buena soldado, hemos ganado")
	else:
		#Algoritmo Eleccion Misil Usuario
		time.sleep(0.5)
		print("\nLanza tu misil soldado!")

		MisilUsuario= input("Elige un punto donde mandar tu misil:")
		time.sleep(0.5)
		print ("Mandaste tu misil al punto " + str(MisilUsuario))

		if MisilUsuario in EComputadora2:
			time.sleep(0.5)
			print ("\nExcelente soldado, has derrivado su barco en el punto " + str(EComputadora2))
			EComputadora2=0
		elif MisilUsuario in EComputadora3:
			time.sleep(0.5)
			print ("\nExcelente soldado, has derrivado su barco en el punto " + str(EComputadora3))
			EComputadora3=0
		else:
			time.sleep(0.5)
			print ("\nFallaste")

		#Algorimo Eleccion Misil Computadora
		time.sleep(1)
		print ("\nTu rival decidira donde mandar su misil")
		MisilComputadora= random.randint(1,36)
		print ("La computadora mando su misil al punto "+ str(MisilComputadora))

		if MisilComputadora in EusuarioB2:
			time.sleep(0.5)
			print ("Nos atacan soldado, han derrivado nuestro barco en el punto " + str(EusuarioB2))
			EusuarioB2=0
		elif MisilComputadora in EusuarioB3:
			time.sleep(0.5)
			print ("Nos atacan soldado, han derrivado nuestro barco en el punto " + str(EusuarioB3))
			EusuarioB3=0
		else:
			time.sleep(0.5)
			print ("Tu rival fallo")







