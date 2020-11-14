from pickleshare import *
from model import *

def newUser(usuario):
	db = PickleShareDB('miBD')
	db[usuario.getUser()] = {'pass': usuario.getPassword()}

def newUserComplete(usuario):
	db = PickleShareDB('miBD')
	db[usuario.getUser()] = {'pass': usuario.getPassword()}
	db[usuario.getUser()] = {'nombre' : usuario.getNombre()}
	db[usuario.getUser()] = {'apellidos' : usuario.getApellidos()}
	db[usuario.getUser()] = {'email' : usuario.getEmail()}

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
