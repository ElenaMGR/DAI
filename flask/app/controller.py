from pickleshare import *
from model import *

def newUser(usuario):
	db = PickleShareDB('miBD')
	db[usuario.getUser()] = {'pass': usuario.getPassword()}

def upSetUser(usuario):
	db = PickleShareDB('miBD')
	db[usuario.getUser()] = {'pass': usuario.getPassword(), 
	'nombre' : usuario.getNombre(),
	'apellidos' : usuario.getApellidos(),
	'email' : usuario.getEmail()}

def validateUser(usuario):
	db = PickleShareDB('miBD')
	if usuario.getUser() in db.keys():
		if usuario.getPassword() == db[usuario.getUser()].get('pass'):
			return True
		else:
			return False

def existUser(usuario):
	db = PickleShareDB('miBD')
	if usuario.getUser() in db.keys():
		return True
	else:
		return False

def getUserInfo(username):
	db = PickleShareDB('miBD')
	usuario = User(username, db[username].get('pass'))
	usuario.setEmail(db[username].get('email'))
	usuario.setNombre(db[username].get('nombre'))
	usuario.setApellidos(db[username].get('apellidos'))

	return usuario