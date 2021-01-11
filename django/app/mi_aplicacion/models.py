from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
	nombre    = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre + ' ' + self.apellidos

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

class Libro(models.Model):
	titulo  = models.CharField(max_length=200)
	autores = models.ManyToManyField(Autor)

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

class Prestamo(models.Model):
	libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
	fecha   = models.DateField(default=timezone.now)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.libro.titulo + ' - ' + self.usuario

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)