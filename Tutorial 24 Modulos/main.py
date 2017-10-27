#forma regular
import calculadora
resultado=calculadora.suma(30,45)
print (resultado)

#importar una sola funcion
from calculadora import resta
resultado= resta(30,45)
print (resultado)

#importar varias funciones
from calculadora import suma,resta

resultado= resta(20,45)
print (resultado)

resultado= suma(20,45)
print (resultado)

#importar todas las funciones de un archivo
from calculadora import *
resultado=suma(50,85)
print (resultado)

#importar una funcion y cambiarle el nombre
from calculadora import suma as x

resultado=x(75,150)
print (resultado)


print (__name__)