# Ejercicio 4

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

f = open("ejercicios/ejercicios/fibonacciEntrada.txt","r")
numero = int(f.read())
f.close()

fo = open("ejercicios/ejercicios/fibonacciSalida.txt","w")
fo.write(str(fibonacci(numero)))
fo.close()

