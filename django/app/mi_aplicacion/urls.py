from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('mostrarLibros', views.mostrarLibros, name='mostrarLibros'),
	path('mostrarAutores', views.mostrarAutores, name='mostrarAutores'),
	path('mostrarPrestamos', views.mostrarPrestamos, name='mostrarPrestamos'),
]