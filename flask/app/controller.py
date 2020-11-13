from pickleshare import *
from model import *

def newUser(usuario):
	db = PickleShareDB('miBD')
	db[usuario.getUser()] = {'pass': usuario.getPassword()}

def validateUser(usuario):
	db = PickleShareDB('miBD')
	if usuario.getUser() in db.keys():
		if usuario.getPassword() == db[usuario.getUser()].get('pass'):
			return True
		else:
			return False
