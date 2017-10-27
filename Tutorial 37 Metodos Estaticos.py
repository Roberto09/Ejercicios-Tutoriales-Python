"""Metodos Estaticos"""
#Los metodos estaticos son simplemente metodos que pertenecen a la clase.
class Circulo:

	#aqui declaramos un metodo estatico con la @staticmethod
	@staticmethod
	def pi():
		return 3.1416

	#funcion principal
	def __init__(self, radio):
		self.radio=radio

	#metodo para cualcular el area
	def area(self):
		#aqui accesamos al staic method con un self.pi()
		return self.radio * self.radio * self.pi()

#Ejecucion del programa
circulo_uno = Circulo(7)
print (circulo_uno.radio)

print (circulo_uno.area())

#El objeto tambien puede adquiere el metodo estatico
print (circulo_uno.pi())