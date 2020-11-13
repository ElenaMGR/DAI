#./app/app.py
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from ejercicios import *
import time

rank = []

@app.route('/')
@app.route('/index')
def index():
	if not 'urls' in session:
		session['urls'] = []
	if not 'username' in session:
		session['username'] = []

	pags_visitadas()
	return render_template('index.html',
	login=session['username'],
	rank=session['urls'])

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
	pags_visitadas()

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
			seleccion = resSeleccion,
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 3 de la Práctica 1
@app.route('/criba/<num>')
def cribaEratostenes(num):
	pags_visitadas()

	if num.isdigit():
		numerosPrimos = criba(int(num))
		numerosPrimos = [str(i) for i in numerosPrimos]
		msg = "Números primos hasta " + num + ": " + (', ').join(numerosPrimos)
	else:
		msg = "Debe introducir un número."

	return render_template('ejercicios.html',
			ejercicio = "Criba de Eratóstenes",
			mensaje = msg,
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 4 de la Práctica 1
@app.route('/fibonacci/<num>')
def fibonacci(num):
	pags_visitadas()

	if num.isdigit():
		sucesion = sfibonacci(int(num))
		msg = "El numero de la sucesión de Fibonacci en la posición " + num + " es: " + str(sucesion)
	else:
		msg = "Debe introducir un número."
	
	return render_template('ejercicios.html',
			ejercicio = "Sucesión de Fibonacci",
			mensaje = msg,
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 5 de la Práctica 1
@app.route('/balanceo/<cadena>')
def balanceo(cadena):
	pags_visitadas()

	return render_template('ejercicios.html',
			ejercicio = "Balanceo",
			mensaje = balanceada(cadena),
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 6 de la Práctica 1
@app.route('/expresiones_regulares/palabraEspMayus/<cadena>')
def erPalabraEspMayus(cadena):
	pags_visitadas()

	return render_template('ejercicios.html',
			ejercicio = "Expresiones regulares",
			mensaje = palabraEspMayus(cadena),
			login=session['username'],
			rank=session['urls'])

@app.route('/expresiones_regulares/correo/<cadena>')
def erCorreo(cadena):
	pags_visitadas()

	return render_template('ejercicios.html',
			ejercicio = "Expresiones regulares",
			mensaje = correo(cadena),
			login=session['username'],
			rank=session['urls'])

@app.route('/expresiones_regulares/tarjeta/<cadena>')
def erTarjeta(cadena):
	pags_visitadas()

	return render_template('ejercicios.html',
			ejercicio = "Expresiones regulares",
			mensaje = tarjeta(cadena),
			login=session['username'],
			rank=session['urls'])

# Muestra una página de error
@app.errorhandler(404)
def error_404(error):
	return render_template('error.html'), 404

# Crear Imágenes Dinámicas
@app.route('/svg')
def random_svg():
	pags_visitadas()

	figuras=['circle', 'rect', 'ellipse']
	colores=['red', 'green', 'blue', 'white', 'orange', 'violet', 'purple', 'yellow', 'fuchsia', 'snow', 'darkRed', 'coral', 'mediumPurple', 'orangeRed', 'navy', 'saddleBrown', 'cyan']

	forma = random.choice(figuras)
	color = random.choice(colores)
	color_relleno = random.choice(colores)

	fig=forma

	if forma=='circle':
		cx = random.randint(50, 400)
		cy = random.randint(50, 200)
		r = random.randint(30, 160)
		fig=fig+' cx='+str(cx)+' cy='+str(cy)+' r='+str(r)

	elif forma=='rect':
		x = random.randint(10, 300)
		y = random.randint(10, 150)
		width = random.randint(50, 400)
		height = random.randint(50, 400)
		fig=fig+' x='+str(x)+' y='+str(y)+' width='+str(width)+' height='+str(height)
	
	elif forma=='ellipse':
		cx = random.randint(50, 300)
		cy = random.randint(50, 150)
		rx = random.randint(50, 300)
		ry = random.randint(50, 150)
		fig=fig+' cx='+str(cx)+' cy='+str(cy)+' rx='+str(rx)+' ry='+str(ry)


	fig=fig+' stroke='+color+' stroke-width=4 fill='+color_relleno

	return render_template('svg.html',
			figura=fig,
			login=session['username'],
			rank=session['urls'])

#########################################################
#														#
#					Práctica 3							#
#														#
#########################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
	pags_visitadas()

	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or \
				request.form['password'] != 'secret':
			error = 'Invalid Username or password'
		else:
			session['username'] = request.form['username']

			# app.logger.info("Error: ")
			# app.logger.info(request.form.getlist('remember'))
			# if request.form.getlist('remember'):
			# 	session['rememberUser'] = request.form['username']

			return redirect(url_for('index'))
	return render_template('login.html',
			error=error,
			login=session['username'],
			rank=session['urls'])

@app.route('/logout', methods=['GET'])
def logout():
	if 'username' in session:
		session.pop('username', None)
	
	if not 'username' in session:
		session['username'] = []

	return render_template('index.html',
			login=session['username'],
			rank=session['urls'])

def pags_visitadas():
	if not request.url in rank[-1:]:
		if len(rank) >= 3:
			del rank[0]
		rank.append(request.url)

	session['urls'] = rank