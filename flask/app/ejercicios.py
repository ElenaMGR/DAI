import random
import re

# Ejercicio 2

def burbuja(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz)-i-1):
			if matriz[j] > matriz[j+1]:
				aux = matriz[j]
				matriz[j] = matriz[j+1]
				matriz[j+1] = aux
	return matriz

def seleccion(matriz):
	for i in range(len(matriz)):
		mini = min(matriz[i:]) #find minimum element
		min_index = matriz[i:].index(mini) #find index of minimum element
		matriz[i + min_index] = matriz[i] #replace element at min_index with first element
		matriz[i] = mini                  #replace first element with min element
	return matriz

# Ejercicio 3

def criba(n):

	noprimos = []

	# iteramos desde 2 hasta la raiz cuadrada de n
	# y desde lo que lleva i, hasta n / i
	# esto nos permite obtener todos los multiplos de i
	# y agregarlos a el conjunto noprimos
	for i in range(2, int(n ** .5) + 1):
		if i not in noprimos:
			for j in range(i, int(n / i) + 1): noprimos.append(i * j)

	# por ultimo creamos una lista con todos los numeros
	# primos desde 2 hasta n
	primos = [p for p in range(2, n + 1) if p not in noprimos]

	return primos

# Ejercicio 4
def sfibonacci(n):
	if n <= 1:
		return n
	else:
		return sfibonacci(n-1) + sfibonacci(n-2)

#Ejercicio 5
def balanceada(cadena):
	cuenta = 0
	msg = ""
	terminado = False
	# Contamos el numero de corchetes abiertos y cerrados. 
	# Comprobamos si en algún momento se han cerrado más que abierto
	for i in range(len(cadena)):
		if (cadena[i] == "["):
			cuenta += 1
		elif (cadena[i] == "]"):
			cuenta -= 1
		
		if (cuenta < 0):
			msg = "¡Demasiados corchetes cerrados!"
			i = range(len(cadena))
			terminado = True

	# Comprobamos si queda alguno abierto
	if (terminado == False):
		if (cuenta > 0):
			msg = "¡Demasiados corchetes abiertos!"
		else:
			msg = "¡La cadena está balanceada!"
	
	return msg

# Ejercicio 6. Expresiones regulares

# Identificar cualquier palabra seguida de un espacio y una única letra mayúscula
def palabraEspMayus(palabra):
	if re.search(r'\b([A-Za-z]+) ([A-Z])\b', palabra):
		return "Palabra seguida de un espacio y una única letra mayúscula encontrada"
	else:
		return "No se ha encontrado una palabra seguida de un espacio y una única letra mayúscula"

# Identificar correos electrónicos válidos
def correo(email):
	if re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b', email):
		return "email correcto"
	else:
		return "email incorrecto"

# Identificar números de tarjeta de crédito cuyos dígitos estén separados 
# por - o espacios en blanco cada paquete de cuatro dígitos
def tarjeta(numero):
	if re.search(r'\b(\d{4} \d{4} \d{4} \d{4})|(\d{4}-\d{4}-\d{4}-\d{4})\b', numero):
		return "Número de tarjeta de crédito correcto"
	else:
		return "Número de tarjeta de crédito incorrecto"