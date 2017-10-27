"""Diccionarios"""
Diccionario={1: "hola", 2: 5, "booleano": True, "lista": [8,2,5,9]}

#Accesar a un valor dentro del diciconario
print (Diccionario[1])

#Accesar a una lista dentro del diciconario
print(Diccionario["lista"][0])

#Agregar nuevo valor
Diccionario["Nuevo"]= False
print (Diccionario)

#Reemplazar un valor existente
Diccionario[1]= False
print (Diccionario)

#Eliminar un valor
del Diccionario[2]
print (Diccionario)

#Obtener un valor del diccionario que quizas no se encuentre dentro de el
valor= Diccionario.get("Altra", 1.80)
print (valor)

#Obtener las llaves de un diccionario
llaves= Diccionario.keys()
print (llaves)

#Obtener las llaves en manera de lista
llaves= list(Diccionario.keys())
print (llaves)

#Obtener valores de un diciconario
valores= Diccionario.values()
print (valores)

#Obtener valores en manera de lista
valores= list(Diccionario.values())
print (valores)


