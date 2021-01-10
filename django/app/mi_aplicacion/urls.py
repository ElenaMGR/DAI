from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('mostrarLibros', views.mostrarLibros, name='mostrarLibros'),
	path('mostrarAutores', views.mostrarAutores, name='mostrarAutores'),
	path('mostrarPrestamos', views.mostrarPrestamos, name='mostrarPrestamos'),
	path('addLibro', views.addLibro, name='addLibro'),
	path('eliminarLibro', views.eliminarLibro, name='eliminarLibro'),
	path('modificarLibro', views.modificarLibro, name='modificarLibro'),
	path('addAutor', views.addAutor, name='addAutor'),
	path('eliminarAutor', views.eliminarAutor, name='eliminarAutor'),
	path('modificarAutor', views.modificarAutor, name='modificarAutor'),
	path('addPrestamo', views.addPrestamo, name='addPrestamo'),
	path('eliminarPrestamo', views.eliminarPrestamo, name='eliminarPrestamo'),
	path('modificarPrestamo', views.modificarPrestamo, name='modificarPrestamo'),
]