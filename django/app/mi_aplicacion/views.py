from django.shortcuts import render, HttpResponse
from .models import Libro, Autor, Prestamo

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World!')

def index(request):
	# Aquí van la las variables para la plantilla
	context = {}
	return render(request,'base.html', context)

def mostrarLibros (request):
	libros = Libro.objects.all()

	#if request.user.is_authenticated:
	#	user_activo = request.user.username
	#	return render(request, 'libros_list.html', {'login': user_activo, 'libros': libros})

	# else:

	context= {'libros': libros}
	return render(request, 'libro.html', context)

def mostrarAutores (request):
	autores = Autor.objects.all()

	context= {'autores': autores}
	return render(request, 'autor.html', context)

def mostrarPrestamos (request):
	prestamos = Prestamo.objects.all()

	context= {'prestamos': prestamos}
	return render(request, 'prestamo.html', context)