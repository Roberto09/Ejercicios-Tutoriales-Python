Contador= 0
Marca= True

#while simple

while Contador <10:
	print (Contador)
	Contador +=1

Contador = 0
#while con else dentro

while Contador <10:
	print (Contador)
	Contador += 1
else:
	print ("El contador ah terminado")

Contador = 0
#while con if dentro

while Contador <10:
	print (Contador)
	Contador +=1
	if Contador ==5:
		print ("Hemos llegado a 5")
else:
	print ("El contador ah terminado")

Contador = 0
#while con continue y break

while Contador <10:
	print (Contador)
	Contador +=1
	if Contador == 5:
		continue
	if Contador ==7:
		break
else:
	print ("El contador ah terminado")

Contador = 0
#While con un limite sin breaks

while Marca: #Mientras Marca se mantenga verdadero se ejecutara el while
	print (Contador)
	Contador +=1
	if Contador == 5:
		continue
	if Contador ==7:
		Marca=False
else:
	print ("El contador ah terminado")