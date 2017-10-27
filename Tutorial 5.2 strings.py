nombre= "Roberto"
edad= "16"

mensaje= "Hola, me llamo " + nombre + " y tengo " + edad + " anos" #1
mensaje2= "Hola, me llamo %s y tengo %s anos" %(nombre,edad) #2
mensaje3= "Hola, me llamo {} y tengo {} anos" .format (nombre,edad) #3

print "1.- " + (mensaje)
print "2.- " + (mensaje2)
print "3.- " + (mensaje3)
