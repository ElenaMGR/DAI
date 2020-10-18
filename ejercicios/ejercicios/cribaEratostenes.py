# Ejercicio 4
# La Criba de Eratóstenes es un sencillo algoritmo que permite encontrar todos
# los números primos menores de un número natural dado.

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

n = input("Introduce número: ")
if n.isdigit():
	print (criba(int(n)))
else:
	print("Debe introducir un número.")