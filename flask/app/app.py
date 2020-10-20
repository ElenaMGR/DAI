#./app/app.py
from flask import Flask
app = Flask(__name__)

from ejercicios import *
import time

@app.route('/')
def hello_world():
	return 'Hello, World!'

#########################################################
#														#
#					Práctica 2							#
#														#
#########################################################

# Muestra una página para el ejercicio 2 de la P1
@app.route('/ordena/<cadena>')
def ordena(cadena):
	lista = cadena.split(',')
	lista = [int(i) for i in lista]

	inicio = time.time()
	listaBurbuja=burbuja(lista[:])
	fin = time.time()
	listaBurbuja = [str(i) for i in listaBurbuja]
	resBurbuja = "Burbuja ha tardado: " + str(fin - inicio) + " segundos"
	listaOrdBurbuja = "Lista ordenada mediante Burbuja: " + (' - ').join(listaBurbuja)

	inicio = time.time()
	listaSeleccion=seleccion(lista[:])
	fin = time.time()
	listaSeleccion = [str(i) for i in listaSeleccion]
	resSeleccion = "Selección ha tardado: " + str(fin - inicio) + " segundos"
	listaOrdSeleccion = "Lista ordenada mediante Selección: " + (' - ').join(listaSeleccion)

	cadenaFinal = "Ordenando..." + (' - ').join(listaBurbuja)
	return cadenaFinal

# Muestra una página para el ejercicio 3 de la P1
@app.route('/criba/<num>')
def cribaEratostenes(num):
	if num.isdigit():
		numerosPrimos = criba(int(num))
		numerosPrimos = [str(i) for i in numerosPrimos]
		return "Números primos hasta " + num + ": " + (', ').join(numerosPrimos)
	else:
		return "Debe introducir un número."

# Muestra una página para el ejercicio 4 de la P1
@app.route('/fibonacci/<num>')
def fibonacci(num):
	if num.isdigit():
		sucesion = sfibonacci(int(num))
		return "El numero de la sucesión de Fibonacci en la posición " + num + " es: " + str(sucesion)
	else:
		return "Debe introducir un número."

# Muestra una página para el ejercicio 5 de la P1
@app.route('/fibonacci/<num>')
def fibonacci(num):
	if num.isdigit():
		sucesion = sfibonacci(int(num))
		return "El numero de la sucesión de Fibonacci en la posición " + num + " es: " + str(sucesion)
	else:
		return "Debe introducir un número."
