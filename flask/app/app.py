#./app/app.py
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from ejercicios import *
from model import *
from controller import *
import time
import random

rank = []
# usuarioAdmin = User('admin', '1234')
# newUser (usuarioAdmin)
numeroAdivina = -1
numeroIntentos = 0

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo

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
		# if request.form['username'] != 'admin' or \
		# 		request.form['password'] != 'secret':
		# 	error = 'Invalid Username or password'
		# else:
		# 	session['username'] = request.form['username']
		usuario = User(request.form['username'], request.form['password'])
		if validateUser(usuario):
			session['username'] = usuario.getUser()
			# app.logger.info("Error: ")
			# app.logger.info(request.form.getlist('remember'))
			# if request.form.getlist('remember'):
			# 	session['rememberUser'] = request.form['username']
			flash('You were successfully logged in')
			return redirect(url_for('index'))

		else:
			error = 'Invalid Username or password'

	db = PickleShareDB('miBD')
	app.logger.info(db['Jose'])

	return render_template('login.html',
			error=error,
			login=session['username'],
			rank=session['urls'])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	pags_visitadas()

	error = None

	if request.method == 'POST':
		usuario = User(request.form['username'], request.form['password'])
		if existUser(usuario):
			error = 'Username already exists'
		else:
			if request.form['password'] != request.form['password2']:
				error = 'Passwords do not match'
			else:
				usuario.setPassword(request.form['password'])
				usuario.setNombre(request.form['nombre'])
				usuario.setApellidos(request.form['apellidos'])
				usuario.setEmail(request.form['email'])
				upSetUser (usuario)
				session['username'] = usuario.getUser()
				
				return redirect(url_for('index'))

	return render_template('signup.html',
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

@app.route('/modify', methods=['GET', 'POST'])
def modify():
	pags_visitadas()

	error = None

	usuario = getUserInfo(session['username'])

	if request.method == 'POST':
		if request.form['password'] != request.form['password2']:
			error = 'Passwords do not match'
		else:
			usuario.setPassword(request.form['password'])
			usuario.setNombre(request.form['nombre'])
			usuario.setApellidos(request.form['apellidos'])
			usuario.setEmail(request.form['email'])
			upSetUser (usuario)

			return redirect(url_for('modify'))

	return render_template('modify.html',
			error=error,
			login=session['username'],
			nombre = usuario.getNombre(),
			apellidos = usuario.getApellidos(),
			email = usuario.getEmail(),
			rank=session['urls'])

@app.route('/adivina', methods=['GET', 'POST'])
def adivina():
	global numeroAdivina
	global numeroIntentos

	if session['urls'][-1][22:40] != 'adivina':
		numeroAdivina = -1

	pags_visitadas()
	
	mensaje = None
	tipoAlert = "warning"

	if numeroAdivina < 0:
		numeroAdivina = random.randint(1,100)
		numeroIntentos = 0
	else:
		numeroIntentos +=1

	app.logger.info("Adivina: " + str(numeroAdivina))

	if numeroIntentos < 10:
		if request.method == 'POST':
			num = int(request.form['adivinaNumero'])
			if num > 100 or num < 1:
				mensaje = "El número tiene que estar en el rango [1-100]."
			elif num == numeroAdivina:
				mensaje = "¡¡Enhorabuena!! ¡¡¡¡Valor encontrado!!!!"
				tipoAlert = "success"
				numeroAdivina = -1
			elif num > numeroAdivina:
				mensaje = "El número buscado es menor que " + str(num)
			elif num < numeroAdivina:
				mensaje = "El número buscado es mayor que " + str(num)
	else:
		tipoAlert = "danger"
		mensaje = "¡Lo siento! No has conseguido adivinar el número tras 10 intentos. ¡El número era " + str(numeroAdivina) + "!"
		numeroAdivina = -1

	return render_template('adivina.html',
			login=session['username'],
			rank=session['urls'],
			mensaje = mensaje,
			tipoAlert = tipoAlert)

def pags_visitadas():
	if not request.url in rank[-1:]:
		if len(rank) >= 3:
			del rank[0]
		rank.append(request.url)

	session['urls'] = rank

# Muestra una página para el ejercicio 3 de la Práctica 1
@app.route('/criba', methods=['GET', 'POST'])
def cribaEratostenesP3():
	pags_visitadas()
	msg = None

	if request.method == 'POST':
		num = int(request.form['valorEjer'])
		numerosPrimos = criba(num)
		numerosPrimos = [str(i) for i in numerosPrimos]
		msg = "Números primos hasta " + str(num) + ": " + (', ').join(numerosPrimos)

	return render_template('ejerciciosP3.html',
			ejercicio = "Criba de Eratóstenes",
			tipoInput = "number",
			mensaje = msg,
			enunciado = "Introduce un número",
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 4 de la Práctica 1
@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacciP3():
	pags_visitadas()
	msg = None

	if request.method == 'POST':
		num = int(request.form['valorEjer'])
		sucesion = sfibonacci(num)
		msg = "El numero de la sucesión de Fibonacci en la posición " + str(num) + " es: " + str(sucesion)
	
	return render_template('ejerciciosP3.html',
			ejercicio = "Sucesión de Fibonacci",
			tipoInput = "number",
			enunciado = "Introduce un número",
			mensaje = msg,
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 5 de la Práctica 1
@app.route('/balanceo', methods=['GET', 'POST'])
def balanceoP3():
	pags_visitadas()
	mensaje = None

	if request.method == 'POST':
		cadena = request.form['valorEjer']
		mensaje = balanceada(cadena)

	return render_template('ejerciciosP3.html',
			ejercicio = "Balanceo",
			tipoInput = "text",
			enunciado = "Introduce una cadena",
			mensaje = mensaje,
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 6 de la Práctica 1
@app.route('/expresiones_regulares/palabraEspMayus', methods=['GET', 'POST'])
def erPalabraEspMayusP3():
	pags_visitadas()
	mensaje = None

	if request.method == 'POST':
		cadena = request.form['valorEjer']
		mensaje = palabraEspMayus(cadena)

	return render_template('ejerciciosP3.html',
			ejercicio = "Expresiones regulares",
			tipoInput = "text",
			mensaje = mensaje,
			enunciado = "Introduce una palabra",
			login=session['username'],
			rank=session['urls'])

@app.route('/expresiones_regulares/correo', methods=['GET', 'POST'])
def erCorreoP3():
	pags_visitadas()
	mensaje = None

	if request.method == 'POST':
		cadena = request.form['valorEjer']
		mensaje = correo(cadena)

	return render_template('ejerciciosP3.html',
			ejercicio = "Expresiones regulares",
			tipoInput = "text",
			enunciado = "Introduce un correo",
			mensaje = mensaje,
			login=session['username'],
			rank=session['urls'])

@app.route('/expresiones_regulares/tarjeta', methods=['GET', 'POST'])
def erTarjetaP3():
	pags_visitadas()
	mensaje = None

	if request.method == 'POST':
		cadena = request.form['valorEjer']
		mensaje = tarjeta(cadena)

	return render_template('ejerciciosP3.html',
			ejercicio = "Expresiones regulares",
			tipoInput = "text",
			enunciado = "Introduce un número de tarjeta",
			mensaje = mensaje,
			login=session['username'],
			rank=session['urls'])

# Muestra una página para el ejercicio 2 de la Práctica 1
@app.route('/ordena', methods=['GET', 'POST'])
def ordenaP3():
	pags_visitadas()
	mensaje = None
	original = None
	ordenada = None
	error = None
	lista = []

	if request.method == 'POST':
		cadena = request.form['valorEjer']

		lista = cadena.split(',')
		lista = [int(i) for i in lista]

		inicio = time.time()
		listaBurbuja=burbuja(lista[:])
		fin = time.time()
		listaBurbuja = [str(i) for i in listaBurbuja]
		resBurbuja = "Burbuja ha tardado: " + str(fin - inicio) + " segundos. "

		inicio = time.time()
		listaSeleccion=seleccion(lista[:])
		fin = time.time()
		listaSeleccion = [str(i) for i in listaSeleccion]
		resSeleccion = "Selección ha tardado: " + str(fin - inicio) + " segundos. "

		ordenada =(' - ').join(listaBurbuja)

		mensaje = "Matriz Ordenada: "  + ordenada
		error = "Tiempos de ejecución: " + resBurbuja + resSeleccion

	#return cadenaFinal
	lista = [str(i) for i in lista]
	return render_template('ejerciciosP3.html',
			ejercicio = "Ordenación de matrices",
			enunciado = "Introduce números separados por ,",
			tipoInput = "text",
			mensaje = mensaje,
			error = error,
			tipoAlert = 'warning',
			login=session['username'],
			rank=session['urls'])

#########################################################
#														#
#					Práctica 4							#
#														#
#########################################################

@app.route('/practica4', methods=['GET', 'POST'])
def practica4():
	pags_visitadas()
	mensaje = None
	episodios = None

	if request.method == 'POST':
		# Si estamos haciendo una búsqueda
		if request.form['search']:
			busqueda = request.form['search']
			# busqueda = busqueda.capitalize()
			# app.logger.debug("Search: "+ busqueda)
			busqueda = {'$regex': '.*'+ busqueda +'.*'}
			episodios = db.samples_friends.find({"name": busqueda})


	# Encontramos los documentos de la coleccion "samples_friends"
	if episodios is None:
		episodios = db.samples_friends.find() # devuelve un cursor(*), no una lista ni un iterador

	lista_episodios = []
	for episodio in episodios:
		# app.logger.debug(episodio) # salida consola
		lista_episodios.append(episodio)

	lista_cabeceras = ['name','season','number','airdate','airtime','airstamp','runtime']
	# for cabecera in lista_episodios[0].keys():
	# 	if not cabecera.startswith('_'):
	# 		lista_cabeceras.append(cabecera)
	# 		app.logger.debug("Cabeceras: " + str(cabecera))


	# a los templates de Jinja hay que pasarle una lista, no el cursor

	return render_template('practica4.html',
			episodios=lista_episodios,
			cabeceras = lista_cabeceras,
			mensaje = mensaje,
			login=session['username'],
			rank=session['urls'])


# Añadir nuevo item a la base de datos
@app.route('/newBD', methods=['GET', 'POST'])
def newBD():
	pags_visitadas()

	error = None

	if request.method == 'POST':
		name = request.form['nombre']
		season = request.form['season']
		number = request.form['numberEp']
		airdate = request.form['airdate']
		airtime = request.form['airtime']
		airstamp = request.form['airstamp']
		runtime = request.form['runtime']

		db.samples_friends.insert_one({'name': name, 'season': season, 'number': number,
				'airdate': airdate, 'airtime': airtime, 'airstamp': airstamp, 'runtime': runtime})

		return redirect(url_for('practica4'))

	return render_template('newBD.html',
			error=error,
			login=session['username'],
			rank=session['urls'])

# Modificar base de datos
@app.route('/updateBD', methods=['GET', 'POST'])
def updateBD():
	pags_visitadas()

	error = None

	if request.method == 'GET':

		identify = request.args.get('id_ep')

		if identify is not None:

			episodio = db.samples_friends.find_one({"_id": ObjectId(identify)})
			app.logger.debug("Modificar: " + identify)


	if request.method == 'POST':
		
		name = request.form['nombre']
		season = request.form['season']
		number = request.form['numberEp']
		airdate = request.form['airdate']
		airtime = request.form['airtime']
		airstamp = request.form['airstamp']
		runtime = request.form['runtime']

		old_values = db.samples_friends.find_one({"_id": ObjectId(request.form['id_ep'])})
		update = {"$set": {'name': name, 'season': season, 'number': number,
				'airdate': airdate, 'airtime': airtime, 'airstamp': airstamp, 'runtime': runtime}}

		result = db.samples_friends.update_one(old_values, update)

		app.logger.debug("Actualizando... Encontrados: "+ str(result.matched_count))
		app.logger.debug("Actualizando... Actualizados: "+ str(result.modified_count))

		return redirect(url_for('practica4'))

	return render_template('modifyBD.html',
			episodio = episodio,
			error=error,
			login=session['username'],
			rank=session['urls'])

# Eliminar item de la base de datos
@app.route('/deleteBD', methods=['POST'])
def deleteBD():
	if request.method == 'POST':
		identify = request.form['id_ep']

		if identify is not None:
			db.samples_friends.delete_one({"_id": ObjectId(identify)})

	return redirect(url_for('practica4'))

#########################################################
#														#
#					Práctica 5							#
#														#
#########################################################

# para devolver una lista (GET), o añadir (POST)
@app.route('/api/movies', methods=['GET', 'POST'])
def api_1():
	if request.method == 'GET':
		# Búsqueda por argumentos
		if request.args:
			lista = []
			if 'year' in request.args:
				movies = db.video_movies.find({"year": request.args['year']})
				for movie in movies:
					lista.append({
						'id':    str(movie.get('_id')), # pasa a string el ObjectId
						'title': movie.get('title'), 
						'year':  movie.get('year'),
						'imdb':  movie.get('imdb')
						})
				if len(lista) == 0:
					return jsonify({'error':'Not found movie with year ' + request.args['year']}), 404
				else: 
					return jsonify(lista)
			elif 'title' in request. args:
				titulo = {'$regex': '.*'+ request.args['title'] +'.*'}
				movies = db.video_movies.find({"title": titulo})
				for movie in movies:
					lista.append({
						'id':    str(movie.get('_id')), # pasa a string el ObjectId
						'title': movie.get('title'), 
						'year':  movie.get('year'),
						'imdb':  movie.get('imdb')
						})
				if len(lista) == 0:
					return jsonify({'error':'Not found movie with title ' + request.args['title']}), 404
				else: 
					return jsonify(lista)
			elif 'imdb' in request. args:
				movies = db.video_movies.find({"imdb": request.args['imdb']})
				for movie in movies:
					lista.append({
						'id':    str(movie.get('_id')), # pasa a string el ObjectId
						'title': movie.get('title'), 
						'year':  movie.get('year'),
						'imdb':  movie.get('imdb')
						})
				if len(lista) == 0:
					return jsonify({'error':'Not found movie with imdb ' + request.args['imdb']}), 404
				else: 
					return jsonify(lista)
		else:
			lista = []
			movies = db.video_movies.find().sort('year')
			for movie in movies:
				lista.append({
					'id':    str(movie.get('_id')), # pasa a string el ObjectId
					'title': movie.get('title'), 
					'year':  movie.get('year'),
					'imdb':  movie.get('imdb')
					})
			return jsonify(lista)

	if request.method == 'POST':
		# app.logger.debug(request.json)
		nuevo = {
			'title': request.json['title'] if 'title' in request.json else '',
			'year': request.json['year'] if 'year' in request.json else '',
			'imdb': request.json['imdb'] if 'imdb' in request.json else ''
		}

		db.video_movies.insert_one(nuevo)
		# app.logger.debug(nuevo)
		nuevo['_id'] = str(nuevo['_id'])
		return jsonify(nuevo)



# para devolver una, modificar o borrar
@app.route('/api/movies/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
	if request.method == 'GET':
		try:
			movie = db.video_movies.find_one({'_id':ObjectId(id)})
			return jsonify({
				'id':    id,
				'title': movie.get('title'), 
				'year':  movie.get('year'),
				'imdb':  movie.get('imdb')
			})
		except:
			return jsonify({'error':'Not found'}), 404

	if request.method == 'PUT':
		try:
			movie = db.video_movies.find_one({'_id':ObjectId(id)})

			update = {
				'title': request.json['title'] if 'title' in request.json else movie['title'],
				'year': request.json['year'] if 'year' in request.json else movie['year'],
				'imdb': request.json['imdb'] if 'imdb' in request.json else movie['imdb']
			}

			result = db.video_movies.update_one(movie, {"$set": update})

			if result is None:
				return jsonify({'error':'Not Update'}), 419

			else:
				return jsonify({
					'id':    id,
					'title': update.get('title'), 
					'year':  update.get('year'),
					'imdb':  update.get('imdb')
				})
		except:
			return jsonify({'error':'Not found'}), 404

	if request.method == 'DELETE':
		try:
			result = db.video_movies.delete_one({'_id':ObjectId(id)})

			if result is None:
				return jsonify({'error':'Not Delete'}), 419
			else:
				return jsonify({
					'id':    id
				})
		except:
			return jsonify({'error':'Not found'}), 404