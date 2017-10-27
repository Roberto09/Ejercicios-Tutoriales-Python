"""librerias de python"""

"""random"""
import random

#generar numero aleatorio
valor= random.randint(0,10)
print (valor)

#obetner un valor aleatorio de una lista

lista= [1, True, "Hola", 8.20]
print (lista)
valor= random.choice(lista)
print (valor)

#Mezclar el orden de una lista
random.shuffle(lista)
print (lista)

"""daytime"""
import datetime
#nos dice que dia y hora es hoy en este exacto momento
diayhora= datetime.datetime.now()
print (diayhora)

"""sys"""
import sys
import time
#generar barra de progreso simple
for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" %i)
	sys.stdout.flush


