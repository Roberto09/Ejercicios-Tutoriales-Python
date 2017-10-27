"""Init"""
#El __init__ es un metodo que sirve para iniciar con ciertos atributos declarados dentro de este sin nececidad de que tengan un valor predeterminado

#Declaracion de clase
class Lapiz():
	#Declaracion metodo init (parametros con valor predeterminado asignado)
	def __init__(self,color ="Amarillo", contiene_borrador=False, usa_grafito=True):
		self.color= color
		self.contiene_borrador= contiene_borrador
		self.usa_grafito= usa_grafito

	#Funcion para dibujar (debe ser llamada)
	def dibujar(self):
		print("El Lapiz esta dibujando")

	#Funcion para borrar (debe ser llamada)
	def borrar(self):
		if self.contiene_borrador:
			print("El Lapiz esta borrando")
		else:
			print("El Lapiz no puede borrar ya que no tiene borrador")

#Asignacion de clase a objetos con parametros
lapiz_generico_sin_borrador=Lapiz()
lapiz_generico_con_borrador=Lapiz("Amarillo",True)

#llamar funciones objeto 1
lapiz_generico_sin_borrador.borrar()
lapiz_generico_sin_borrador.dibujar()

#llamar funciones objeto 2
lapiz_generico_con_borrador.borrar()
lapiz_generico_con_borrador.dibujar()
