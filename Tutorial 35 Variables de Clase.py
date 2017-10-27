"""Variables de Clase"""
#Son variables que le pertenecen a la clase pero son tambien adquiridas por los objetos

class Circulo:

	#variable de clase
	pi=3.1415

	def __init__(self, radio):
		self.radio=radio

	def area(self):
		return self.radio * self.radio * self.pi

#podemos accesar a esta variable desde la clase
print(Circulo.pi)

#asignacion de clase a objetos
circulo_uno=Circulo(4)
circulo_dos=Circulo(3)

#accesar a metodo de objeto
print (circulo_uno.area())
print (circulo_dos.area())

#imprimir variable de clase adquirida por objeto
print (circulo_uno.pi)
print (circulo_dos.pi)

#modificando variable de clase desde la clase
Circulo.pi=20

print (Circulo.pi)
