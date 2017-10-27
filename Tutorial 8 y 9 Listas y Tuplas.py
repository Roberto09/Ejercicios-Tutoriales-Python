lista= ["Hola", 15, 10.5, True]

#punto especifico
print (lista[2])

#append
lista.append (8)
print (lista)

#insert
lista.insert(1,"Mundo")
print (lista)

#remove
lista.remove(15)
print (lista)

#pop
lista.pop()
print (lista)

"""Numeros"""
lista2= [1,3,5,8,6,4,2,3,1,5]

#sort
lista2.sort()
print (lista2)

#sort reverse
lista2.sort(reverse = True)
print (lista2)

ListaA= [21,22]
ListaB= [31,34]

#extend
ListaA.extend(ListaB)
print ListaA

#append
ListaB.append(ListaA)
print ListaB

"""Tuplas"""
#listas que no se pueden modifiar

listaTupla= ("Hola", 15, 10.5, True)
#mismas propiedades pero es inmutable

ListaR= listaTupla[0:3]
print (ListaR)


