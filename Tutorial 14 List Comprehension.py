"""List Comprehension"""

#Sin List Comprehension

lista= []

for x in range(0,101):
	lista.append(x)

print (lista)


#Ejemplo 1 LC Lista

lista= [ x for x in range(0,101) if x%2 ==0]

print (lista)


#Ejemplo 1 LC Tupla

Tupla=  tuple((x for x in range(0,101) if x%2 ==0))
print (Tupla)


#Ejemplo 1 LC Diccionario

Diccionario= {indice:x for indice,x in enumerate(lista)}
print (Diccionario)


#Ejemplo 1 LC Diccionario (Con condicional)

Diccionario= {indice:x for indice,x in enumerate(lista) if indice<10}
print (Diccionario)
