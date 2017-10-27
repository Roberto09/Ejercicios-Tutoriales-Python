"""numeros primos"""
print ("Elige el entre que numeros quieres encontrar los numeros primos")
ninicial= input("Numero inicial: ")
nfinal= input("Numero final: ")

def alg(p):
	z=True
	for n in range(2,(p/2)+1):
		y=float(p)%float(n)
		if y != 0:
			continue
		else:
			z=False
			break
	return z

for x in range(ninicial,nfinal):
	if alg(x):
		print(x)




