"""Calculadora de peso en otros planetas"""
while True:
	x=True
	y=True
	DiccionarioP={"Venus":8.87, "Tierra":9.78, "Marte":3.72, "Jupiter":22.88, "Saturno":9.05, "Urano":7.77, "Neptuno":11, "Pluton":0.4}
	
	print ("\n-------------------------------\nIntroduce tu peso en kg")

	while x:
		PUsuario= raw_input()
		try:
			PUsuario=float(PUsuario)
			x=False
		except ValueError:
			print("intnentelo denuevo, utilice solo numeros")	

	print ("Tu peso es "+str(PUsuario)+"kg")

	print ("""
En que planeta quieres saber tu peso?
Introduce el nombre de uno de los siguienes planetas:
Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton""")
	while y:
		PlaUsuario= raw_input()
		if PlaUsuario in (DiccionarioP.keys()):
			y=False
		else:
			print ("Lo escribio mal, intentelo denuevo")

	PUsuario= PUsuario/9.78

	def Peso (Planeta):
		return PUsuario*Planeta

	resultado= Peso(DiccionarioP[PlaUsuario])
	print ("Pesas " + str(resultado) + "Kg en " + PlaUsuario)

