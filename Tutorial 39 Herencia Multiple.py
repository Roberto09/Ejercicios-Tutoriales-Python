"""Herencia Multiple"""
#Nos sirve para que alguna clase adquiera propiedades de una o mas clases

#Clase Muestra
class Felino:
	nombre=""
	def mostrar_nombre(self):
		print (self.nombre)

#Clase Muestra
class Mascota:
	def es_domestico(self):
		return True

#Clase que hereda las propiedades de 2 clases
class Gato(Felino,Mascota):
	def __init__ (self, color_pelog):
		self.color_pelo=color_pelog


#asignacion de clase(con parametro) a objeto
gatito=Gato("cafe")

#propiedad de gatito adquirida de clase Gato
print (gatito.color_pelo)


#propiedad de gatito aquirida de clase Felino
gatito.nombre="Max"
gatito.mostrar_nombre()


#propiedad de gatito adquirida de clase Mascota
print (gatito.es_domestico())
