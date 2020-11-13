class User():
	def __init__ (self, username, password):
		self.username = username
		self.password = password
		self.nombre = ""
		self.apellidos = ""
		self.email = ""

	def setNombre (self, nombre):
		self.nombre = nombre

	def setApellidos (self, apellidos):
		self.apellidos = apellidos

	def setEmail (self, email):
		self.email = email

	def getNombre (self):
		return self.nombre

	def getApellidos (self):
		return self.apellidos

	def getEmail (self):
		return self.email

	def getUser (self):
		return self.username
	
	def getPassword (self):
		return self.password