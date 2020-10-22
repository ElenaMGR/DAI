#./app/app.py
from flask import Flask, render_template
app = Flask(__name__)

from ejercicios import *
import time

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/hello')
def hello_world():
	return 'Hello, World!'

#########################################################
#														#
#					Práctica 2							#
#														#
#########################################################

# Muestra una página para el ejercicio 2 de la Práctica 1
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

# Muestra una página para el ejercicio 3 de la Práctica 1
@app.route('/criba/<num>')
def cribaEratostenes(num):
	if num.isdigit():
		numerosPrimos = criba(int(num))
		numerosPrimos = [str(i) for i in numerosPrimos]
		return "Números primos hasta " + num + ": " + (', ').join(numerosPrimos)
	else:
		return "Debe introducir un número."

# Muestra una página para el ejercicio 4 de la Práctica 1
@app.route('/fibonacci/<num>')
def fibonacci(num):
	if num.isdigit():
		sucesion = sfibonacci(int(num))
		return "El numero de la sucesión de Fibonacci en la posición " + num + " es: " + str(sucesion)
	else:
		return "Debe introducir un número."

# Muestra una página para el ejercicio 5 de la Práctica 1
@app.route('/balanceo/<cadena>')
def balanceo(cadena):
	return balanceada(cadena)

# Muestra una página para el ejercicio 6 de la Práctica 1
@app.route('/expresiones_regulares/palabraEspMayus/<cadena>')
def erPalabraEspMayus(cadena):
	return palabraEspMayus(cadena)

@app.route('/expresiones_regulares/correo/<cadena>')
def erCorreo(cadena):
	return correo(cadena)

@app.route('/expresiones_regulares/tarjeta/<cadena>')
def erTarjeta(cadena):
	return tarjeta(cadena)

# Muestra una página de error
@app.errorhandler(404)
def error_404(error):
	return "Error 404, page not found", 404

