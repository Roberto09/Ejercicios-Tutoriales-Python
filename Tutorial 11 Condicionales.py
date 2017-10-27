Nombre= "Roberto"
Edad= 16


# Condicional simple
if Nombre == "Roberto":
	print ("Tu nombre es Roberto")

# Condicional con multiples acciones
if Nombre == "Roberto":
	print ("Tu nombre es Roberto")
	print ("Hola")

#else (Cunado quieres que suceda un accion si la original no se cumple)
if Nombre == "Alberto":
	print ("Tu nombre es Alberto")
else:
	print ("Desconozco tu nomrbe")

#elif (Multiples condicionales dentro de una)
if Nombre == "Alberto":
	print ("Tu nombre es Alberto")
elif Nombre == "Roberto":
	print ("Tu nombre es Roberto")
else:
	print ("Desconozco tu nomrbe")

#pass (Conoces la condicional que debes programar pero no la acicon que debe realizar)
if Nombre == "Alberto":
	pass
else:
	print ("Desconozco tu nomrbe")

#condicionales > < <= >= != ==
Altura= 1.70

if Altura > 1.60: #mayor que
	print ("Eres alto")
elif Altura < 1.60: #menor que
	print ("Eres bajo")
else:
	print ("Pues cuanto mides?")


if Altura <= 1.60: #menor que o igual
	print ("Eres bajo")
elif Altura >=1.80: #mayor que o igual
	print ("Eres alto")
elif Altura >1.60<1.80: #mayor que x & menor que y
	print ("Eres intermedio")
else:
	print ("Pues cuanto mides?")

if Altura != 1.80: #no es igual a
	print ("No mides 1.80")
else:
	print ("Pues cuanto mides?")

if Altura == 1.80: #no es igual a
	print ("Mides 1.80")
else:
	print ("Pues cuanto mides?")

#Apoyos "and" y "or"

Comida= "Manzana"
Postre= "Brocolli"

if Comida == "Manzana" and Postre == "Brocolli" : #si las 2 son ciertas se cumple
	print ("Comes Saludable")
else:
	print ("Come mas saludable")

if Comida == "Pizza" or Postre == "Brocolli" : #si 1 es cierta se cumple
	print ("Comes Saludable")
else:
	print ("Come mas saludable")	
