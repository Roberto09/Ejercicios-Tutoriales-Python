"""For"""

#Ejemplo 1

for valor in range (0,10):
	print ("hola")
#Esto hara que se imprima hola 10 veces hola ya que el valor se repetira for 0-9 times por asi decirlo.



#Ejemplo 2

lista= [2,10,9,0,8,2,0,5,0,45,120,1]

for valor in lista:
	print ("Hola")
#Esto hara que por cada valor que haya dentro de la lista se imripma hola.



#Ejemplo 3

lista= [2,10,9,0,8,2,0,5,0,45,120,1]

for valor in lista:
	print (valor)
#Esto hara que cada vez que se repita el ciclo (numero de valores que hay dentro de la lista)
#se imprima dicho valor en la lista, es decir, imprimira la lista.



#Ejemplo 4

indice= 0

for x in lista:
	print (indice, x)
	indice +=1
#Esto hara que el ciclo se repita por x veces y x tomara el valor de cada numero en la lista hasta que termine.
#Entonces esto se repetira 12 veces recorriendo cada valor de la lista. Ademas declaramos el indice como 0 y cada vez
#que se repite el ciclo le sumamos uno. Por ende, si imprimimos el indice,x hara que nos imprima la numeracion
#del 0 al 11 con cada uno de los 12 valores de la lista (asignados a "x") separados por una coma.



#Ejemplo 5

for indice,x in enumerate(lista):
	print (indice, x)

#Esto es una manera mas sencilla de hacer el ejemplo 4. Esto funciona por que la funcion enumerate nos genera 2 valores
#los cuales son la enumeracion empezando desde el 0 hasta el numero de valores que haya dentro de nuestra lista y la lista en si.
#estos valores son asignados a la variable indice y la variable x; indice representando la enumeracion de la lista
# y x representando los valores en la lista. Posteriormente se imprimen separados en una coma y ya que el ciclo solo se imrpime por
#el numero de valores que hay dento de la lista (x) se imprimira la enumeracion de cada numero de la lista por cada numero existente
#en ella.


#Ejemplo 6

for x in "Hola":
	print x

#Esto hara que el ciclo se repita por x numero de letras que tenga el string, en este caso: Hola.
#Posteriormente, ya que x tomara el valor de cada letra del string, al momento de imrpimirlo, este nos
#imprimira cada letra del string pues convenientemente este ciclo se repetira 4 veces (x= cada letra del string) asignando a x cada letra
#del string la cual sera impresa hasta que termine el cilo imprimiendonos asi "Hola".


#Ejemplo 7

diccionario= {"a":1, "b":2, "c":3}

for llave, valor in diccionario.items():
	print (llave, valor)

#Primero que nada hemos hecho un diccionario del cual obtendremos los valores, posterior mente es necesario recalcar que la funcion
#diccionario.items nos regreara dos valores los cuales seran asignados a las variables llave y valor. Ya que hay 3 items en el
#diccionario el ciclo se repetira 3 veces tomando en cada una de ellas el valor correspondiente e imprimendo las variables previamente
#mecionadas separadas por una coma asi generandonos una tipo "lista impresa" donde se nos reflejara la cada llave separada por una coma
#junto a cada valor de el diccionario