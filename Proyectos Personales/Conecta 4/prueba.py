lista=[1,2,3,10,9,8,29,30,31,32,12,18,24,30]

lista2=[1,2,3,4,5,6,
7,8,9,10,11,12,
13,14,15,16,17,18,
19,20,21,22,23,24,
25,26,27,28,29,30,
31,32,33,34,35,36]

Nverticales=[1,2,3,7,8,9,13,14,15,19,20,21,25,26,27,31,32,33]
EspaciosD=[1,2,3,4,5,6]
EspaciosU=[]
#Limite de elecciones

while True:
	x=True
	while x==True:
		print("Los espacios Disponibles son")
		print(EspaciosD)
		
		print("Los espacios Utilizados son")
		print(EspaciosU)
		EUsuario=input("Elige un numero: ")
		EspaciosD.remove(EUsuario)
		EspaciosD.append(EUsuario+6)







"""
#Ganador o Perdedor
for x in lista2:
	a=x
	b=x+1
	c=x+2
	d=x+3
	if x in Nverticales and a in lista and b in lista and c in lista and d in lista:
		print("ganaste")
		break
	e=x
	f=x+6
	g=x+12
	h=x+18
	if e in lista and f in lista and g in lista and h in lista:
		print("ganaste")
		break
"""
