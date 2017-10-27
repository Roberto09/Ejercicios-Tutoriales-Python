"""Herencia"""
#La herencia nos permite asignar las propiedades/atributos/metodos de clases ya existentes a otras clases.

#Clase padre la cual heredara a otras clases
class Felino:
	#propiedad puede ser utilizada
	@property
	def garras(self):
		return True

	#metodo puede ser utilizado
	def cazar (self):
		print ("El animal esta casando.")

	#metodo privado NO puede ser utilizado por otras clases que hayan heredado esta.
	def __es_agresivo(self):
		return True



#Clase que heredara propiedades de la clase padre
class Gato(Felino):
	#Puedes utilizar las propiedades de una clase dentro de la clase que las heredo
	#Utilizar metodo heredado para madarlo a llamar dentro de otro metodo en la misma clase
	def gato_cazando(self):
		self.cazar()


#Clase que heredara propiedades de la clase padre
class Jaguar(Felino):

	#Error ya que es un atributo privado de la calse padre a la cual no podemos accesar
	def agresivo(self):
		return self.__es_agresivo()


#Asignacion de clases a objetos
gatito=Gato()
jaguarito=Jaguar()


#Llamar a ejecutar metodo creado dentro de la clase gato.
gatito.gato_cazando()

#Imprimir valor de retorno de propiedad>metodo heredado de la clase padre
print(jaguarito.garras)


"""Herencia de multiples niveles"""
class Abuelo:
	@property
	def valor(self):
		return "Esto es herencia de la clase Abuelo"

class Hijo(Abuelo):
	pass

class Nieto(Hijo):
	pass

Hijito=Hijo()
Nietito=Nieto()




print (Hijito.valor)
print (Nietito.valor)


#Error ya que estoy tratando de obtener un atributo privado
#-------------------------------print(jaguarito.agresivo())