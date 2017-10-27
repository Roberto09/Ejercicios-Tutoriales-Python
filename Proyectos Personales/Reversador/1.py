eusuario=raw_input("escribe algo: ")
lista=[]

for x in eusuario:
	lista.append(x)

n=len(lista)-1
lista2=[]

while n>=0:
	lista2.append(lista[n])
	n=n-1

nfrase=""

for x in lista2:
	nfrase=nfrase+x

print(nfrase)