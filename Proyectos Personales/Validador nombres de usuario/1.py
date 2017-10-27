while True:
	nombre=raw_input("introduce tu nombre: ")

	#validacion cuantas letras tiene el nombre
	def largo ():
		larg=len(nombre)
		if larg<6:
			print ("error, el nombre de usuario debe ser mayor a 6 digitos")
			return False
		elif larg>12:
			print ("error, el nombre de usuario debe ser menor a 12 digitos")
			return False
		else:
			return True

	#validaicon de caracteres
	def caracteres ():
		cvalidos=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",'1','2','3','4','5','6','7','8','9','0']
		for x in nombre.lower():
			if x not in cvalidos:
				print("Tu nombre debe solo contener letras o numeros")
				return False
				break
			else:
				continue
		return True		
	
	r1=largo()
	r2=caracteres()
	
	if r1==True and r2==True:
		print("nombre valido")
		break
	else:
		continue



