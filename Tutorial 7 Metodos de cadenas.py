Nombre= "Roberto"
Apeido= "Garcia"

Completo= "{b} {a}" .format(a=Nombre, b=Apeido)
print (Completo)

minusculas= Completo.lower()
print (minusculas)

mayusculas= Completo.upper()
print (mayusculas)

Encontrar= Completo.find("Garcia")
print (Encontrar)

Contador= Completo.count("r")
print (Contador)

Remplazar= Completo.replace("o","w")
print (Remplazar)

Nombre= "Roberto"
Apeido= "Garcia"
Locacion= "Mexico"

Completo2= "{} {} {}" .format(Nombre, Apeido, Locacion)

Separar= Completo2.split( )

print (Separar)
