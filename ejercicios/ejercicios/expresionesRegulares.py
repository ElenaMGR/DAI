# Ejercicio 6

import re

# Identificar cualquier palabra seguida de un espacio y una única letra mayúscula
def palabraEspMayus(palabra):
	return re.search(r'\b([A-Za-z]+) ([A-Z])\b', palabra)

# Identificar correos electrónicos válidos
def correo(email):
	return re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b', email)

# Identificar números de tarjeta de crédito cuyos dígitos estén separados 
# por - o espacios en blanco cada paquete de cuatro dígitos
def tarjeta(numero):
	return re.search(r'\b(\d{4} \d{4} \d{4} \d{4})|(\d{4}-\d{4}-\d{4}-\d{4})\b', numero)

palabra = input("Introduce texto: ")

if palabraEspMayus(palabra):
	print("Correcto")
else:
	print("Incorrecto")

email = input("Introduce email: ")

if correo(email):
	print("Correcto")
else:
	print("Incorrecto")

numero = input("Introduce numero tarjeta: ")

if tarjeta(numero):
	print("Correcto")
else:
	print("Incorrecto")