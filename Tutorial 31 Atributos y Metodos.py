"""Atributos y Metodos"""
#Los atributos son las caracteristicas de un objeto
#Los metodos son las acciones que realiza un objeto

#declaracion de la clase
class Lapiz ():
	#declaracion de los atributos
	color= "Amarillo"
	borrador= False
	largo=2

	#declaracion de los metodos
	def puede_borrar(self):
		return self.borrador

	def borrar(self):
		if self.puede_borrar():
			print("El Lapiz se encuentra borrando")
		else:
			print("El lapiz no puede borrar")

	def escribir(self):
		print("El Lapiz esta escribiendo")

#asignacion de clase a objeto/llamar metodo de un objeto/cambiar atributo de un objeto
lapiz_generico=Lapiz()
lapiz_generico.borrar()
lapiz_generico.borrador=True
lapiz_generico.borrar()
lapiz_generico.escribir()
