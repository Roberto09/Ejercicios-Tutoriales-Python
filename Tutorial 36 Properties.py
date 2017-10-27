"""Properties"""
#Las properties nos permiten trabajar con los atributos privados de una clase u objeto y nos permiten trabajar con returns de funciones como si fueran simples atributos.


#Defininmos la clase
class Usuario:

	#definimos nuestra funcion principal
	def __init__ (self, username, password, email):
		self.username=username
		self.__password=self.__generar_password(password)
		self.email=email


	#definimos nuestra funcion para encriptar que sera llamada desde la funcion principal
	def __generar_password(self,password):
		return password.upper()

	#creamos una property que nos regrese el valor de nuestra password privada
	@property
	def password(self):
		return self.__password

	#creamos una property que reciba como parametro un determinado string (por fuera de nuestra clase/bjeto) que cambiara
	#nuestra password original por lo que le asignemos de valor a esta funcion.
	@password.setter
	def password_changer(self, valor):
		self.__password=self.__generar_password(valor)



#asignacion de clase a objeto
eduardo= Usuario("eduardo","eduardo123","eduardo@gmail.com")
#imprimir atributo privado de objeto mediante una property llamada password
print (eduardo.password)

#cambiar atributo privado de un objeto utilizando una property
eduardo.password_changer="Nueva password"
#imprimir nuevo valor de password despues de haberlo cambiado con la propery password_changer
print (eduardo.password)



"""Como hacerlo funcionar con Python 2.7"""
#https://stackoverflow.com/questions/16502133/python-property-decorator-not-working-why