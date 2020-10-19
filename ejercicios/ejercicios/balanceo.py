# Ejercicio 5
# Comprobar si una secuencia generada aleatoriamente está balanceada

import random

# Generamos una cadena aleatoria de [ y ]
cadena = ""
tam = random.randint(4,8)

for i in range(tam):
	if (random.random() > 0.5):
		cadena += "["
	else:
		cadena += "]"

print ("La cadena aleatoria es %s" % (cadena))

cuenta = 0


# Contamos el numero de corchetes abiertos y cerrados. 
# Comprobamos si en algún momento se han cerrado más que abierto
for i in range(len(cadena)):
	if (cadena[i] == "["):
		cuenta += 1
	else:
		cuenta -= 1
	
	if (cuenta < 0):
		print ("Hay un problema con la cadena en el caracter %d." % (i))	
		exit() 

# Comprobamos si queda alguno abierto
if (cuenta > 0):
	print ("¡Demasiados corchetes abiertos!")
else:
	print ("¡La cadena está balanceada!")