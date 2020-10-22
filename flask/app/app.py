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

	inicio = time.time()
	listaSeleccion=seleccion(lista[:])
	fin = time.time()
	listaSeleccion = [str(i) for i in listaSeleccion]
	resSeleccion = "Selección ha tardado: " + str(fin - inicio) + " segundos"

	#return cadenaFinal
	lista = [str(i) for i in lista]
	return render_template('ordena.html',
			original =(' - ').join(lista), 
			ordenada =(' - ').join(listaBurbuja),
			burbuja = resBurbuja,
			seleccion = resSeleccion)

# Muestra una página para el ejercicio 3 de la Práctica 1
@app.route('/criba/<num>')
def cribaEratostenes(num):
	if num.isdigit():
		numerosPrimos = criba(int(num))
		numerosPrimos = [str(i) for i in numerosPrimos]
		msg = "Números primos hasta " + num + ": " + (', ').join(numerosPrimos)
	else:
		msg = "Debe introducir un número."

	return render_template('ejercicios.html',
			ejercicio = "Criba de Eratóstenes",
			mensaje = msg)

# Muestra una página para el ejercicio 4 de la Práctica 1
@app.route('/fibonacci/<num>')
def fibonacci(num):
	if num.isdigit():
		sucesion = sfibonacci(int(num))
		msg = "El numero de la sucesión de Fibonacci en la posición " + num + " es: " + str(sucesion)
	else:
		msg = "Debe introducir un número."
	
	return render_template('ejercicios.html',
			ejercicio = "Sucesión de Fibonacci",
			mensaje = msg)

# Muestra una página para el ejercicio 5 de la Práctica 1
@app.route('/balanceo/<cadena>')
def balanceo(cadena):
	return render_template('ejercicios.html',
			ejercicio = "Balanceo",
			mensaje = balanceada(cadena))

# Muestra una página para el ejercicio 6 de la Práctica 1
@app.route('/expresiones_regulares/palabraEspMayus/<cadena>')
def erPalabraEspMayus(cadena):
	return render_template('ejercicios.html',
			ejercicio = "Expresiones regulares",
			mensaje = palabraEspMayus(cadena))

@app.route('/expresiones_regulares/correo/<cadena>')
def erCorreo(cadena):
	return render_template('ejercicios.html',
			ejercicio = "Expresiones regulares",
			mensaje = correo(cadena))

@app.route('/expresiones_regulares/tarjeta/<cadena>')
def erTarjeta(cadena):
	return render_template('ejercicios.html',
			ejercicio = "Expresiones regulares",
			mensaje = tarjeta(cadena))

# Muestra una página de error
@app.errorhandler(404)
def error_404(error):
	return render_template('error.html'), 404

# Crear Imágenes Dinámicas
@app.route('/svg')
def random_svg():
	figuras=['circle', 'rect', 'ellipse']
	colores=['red', 'green', 'blue', 'white', 'orange', 'violet', 'purple', 'yellow', 'fuchsia', 'snow', 'darkRed', 'coral', 'mediumPurple', 'orangeRed', 'navy', 'saddleBrown', 'cyan']

	forma = random.choice(figuras)
	color = random.choice(colores)
	color_relleno = random.choice(colores)

	fig=forma

	if forma=='circle':
		cx = random.randint(50, 600)
		cy = random.randint(50, 600)
		r = random.randint(30, 100)
		fig=fig+' cx='+str(cx)+' cy='+str(cy)+' r='+str(r)

	elif forma=='rect':
		x = random.randint(10, 350)
		y = random.randint(10, 150)
		width = random.randint(50, 400)
		height = random.randint(50, 400)
		fig=fig+' x='+str(x)+' y='+str(y)+' width='+str(width)+' height='+str(height)
	
	elif forma=='ellipse':
		cx = random.randint(50, 300)
		cy = random.randint(50, 300)
		rx = random.randint(50, 300)
		ry = random.randint(50, 300)
		fig=fig+' cx='+str(cx)+' cy='+str(cy)+' rx='+str(rx)+' ry='+str(ry)


	fig=fig+' stroke='+color+' stroke-width=4 fill='+color_relleno

	return render_template('svg.html', figura=fig)
