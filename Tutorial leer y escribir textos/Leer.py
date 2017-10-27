#agregar archivos a una lista separandolos por enters y ;

lista1=[]

with open("archivo.txt","r") as archivo:
	for linea in archivo:
		linea=linea.replace("\n","")
		linea=linea.replace(";","")
		lista1.append(linea)

print (lista1)


#atoi home-made method

lista2=[]

for string in lista1:

	#hace un array donde el string es separado por comas y cada elemento es un numero en string
	grupo_numeros=string.split(",")
	
	print (grupo_numeros)
	
	lista_numeros=[]

	#toma cada numero(en forma de string) de el array y lo convierte en un int y lo agrega a una lista que se resetea cada vez que ocurre el for original
	for numero in grupo_numeros:
		numero=int(numero)
		lista_numeros.append(numero)

	lista2.append(lista_numeros)

print (lista2)






#Extra info
for intervalo in lista2:

	if len(intervalo)>1:
		for numero in intervalo:
			pass

	else:
		pass






"""
for intervalo in lista2:
	for numero in intervalo:
		if len(intervalo)>1:
"""




