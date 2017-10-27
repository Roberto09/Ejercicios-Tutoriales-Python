"""Atributos y Metodos privados"""
#Son los atributos y metodos que no queremos que el usuario modifique o tenga acceso a estos

class Usuario:
	def __init__(self, username, password, email):
		self.username=username
		self.password=self.generar_password(password)
		self.email=email

	def generar_password(self, password):
		return password.upper()

eduardo=Usuario("eduardo","eduardo123","eduardo@gmial.com")

print(eduardo.username)
print(eduardo.password)
print(eduardo.email)






#Atributos Privados:
class Usuario1:
	def __init__(self, username, password, email):
		self.username=username
		self.__password=self.generar_password(password)
		self.email=email

	def generar_password(self, password):
		return password.upper()

eduardo=Usuario1("eduardo","eduardo123","eduardo@gmial.com")

print(eduardo.username)
#imposible ya que no se puede accesar al atributo de ninguna forma: print(eduardo.password)
print(eduardo.email)






#Metodos Privados
class Usuario2:
	def __init__(self, username, password, email):
		self.username=username
		self.__password=self.__generar_password(password)
		self.email=email

	def __generar_password(self, password):
		return password.upper()

eduardo=Usuario2("eduardo","eduardo123","eduardo@gmial.com")

print(eduardo.username)
#imposible ya que el metodo es privado: print(eduardo.__generar_password)
print(eduardo.email)



# regresar password con metodos y atributos privados

class Usuario3:
	def __init__(self, username, password, email):
		self.username=username
		self.__password=self.__generar_password(password)
		self.email=email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):
		return self.__password

eduardo=Usuario3("eduardo","eduardo123","eduardo@gmial.com")

print(eduardo.username)
print(eduardo.get_password())
print(eduardo.email)
