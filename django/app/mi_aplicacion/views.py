from django.shortcuts import render, HttpResponse, redirect
from .models import Libro, Autor, Prestamo
from .forms import LibroForm, AutorForm, PrestamoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World!')

def index(request):
	# Aquí van la las variables para la plantilla
	user_activo = request.user.username
	context = {'login': user_activo}
	return render(request,'base.html', context)

def mostrarLibros (request):
	libros = Libro.objects.all()

	#if request.user.is_authenticated:
	#	user_activo = request.user.username
	#	return render(request, 'libros_list.html', {'login': user_activo, 'libros': libros})

	# else:
	user_activo = request.user.username
	context= {'login': user_activo, 'libros': libros}
	return render(request, 'libro.html', context)

def mostrarAutores (request):
	user_activo = request.user.username
	autores = Autor.objects.all()

	context= {'login': user_activo, 'autores': autores}
	return render(request, 'autor.html', context)

def mostrarPrestamos (request):
	user_activo = request.user.username
	prestamos = Prestamo.objects.all()

	context = {'login': user_activo, 'prestamos': prestamos}
	return render(request, 'prestamo.html', context)

def addLibro (request):
	user_activo = request.user.username
	if request.method == 'POST':
		form = LibroForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('mostrarLibros')

	else:
		form = LibroForm()

	context = {'login': user_activo, 'form': form }

	return render(request, 'addLibro.html', context)

def eliminarLibro (request):
	Libro.objects.filter(pk=request.POST.get('pk_libro')).delete()
	return redirect('mostrarLibros')

def modificarLibro (request):
	user_activo = request.user.username
	if request.method == 'POST' and 'modificado' in request.POST:
		form = LibroForm(request.POST)

		if form.is_valid():
			form.pk = request.POST.get('pk_libro')
			form.save()
			Libro.objects.filter(pk=request.POST.get('pk_libro')).delete()

		return redirect('mostrarLibros')

	else:
		pk = request.POST.get('pk_libro')
		libro = Libro.objects.get(pk=pk)
		data = {'titulo': libro.titulo, 'autores': libro.autores.all()}
		form = LibroForm(data)
		context = {'login': user_activo, 'form': form , 'pk_libro' : pk}
		return render(request, 'modificarLibro.html', context)

def addAutor (request):
	user_activo = request.user.username
	if request.method == 'POST':
		form = AutorForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('mostrarAutores')

	else:
		form = AutorForm()

	context = {'login': user_activo, 'form': form }

	return render(request, 'addAutor.html', context)

def eliminarAutor (request):
	user_activo = request.user.username
	Autor.objects.filter(pk=request.POST.get('pk_autor')).delete()
	return redirect('mostrarAutores')

def modificarAutor (request):
	user_activo = request.user.username
	if request.method == 'POST' and 'modificado' in request.POST:
		Autor.objects.filter(pk=request.POST.get('pk_autor')).update(nombre=request.POST.get('nombre'), apellidos=request.POST.get('apellidos'))

		return redirect('mostrarAutores')

	else:
		pk = request.POST.get('pk_autor')
		autor = Autor.objects.get(pk=pk)
		data = {'nombre': autor.nombre, 'apellidos': autor.apellidos}
		form = AutorForm(data)
		context = {'login': user_activo, 'form': form , 'pk_autor' : pk}
		return render(request, 'modificarAutor.html', context)

def addPrestamo (request):
	user_activo = request.user.username
	if request.method == 'POST':
		form = PrestamoForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('mostrarPrestamos')

	else:
		form = PrestamoForm()

	context = {'login': user_activo, 'form': form }

	return render(request, 'addPrestamo.html', context)

def eliminarPrestamo (request):
	user_activo = request.user.username
	Prestamo.objects.filter(pk=request.POST.get('pk_prestamo')).delete()
	return redirect('mostrarPrestamos')

def modificarPrestamo (request):
	user_activo = request.user.username
	if request.method == 'POST' and 'modificado' in request.POST:
		Prestamo.objects.filter(pk=request.POST.get('pk_prestamo')).update(libro=request.POST.get('libro'), fecha=request.POST.get('fecha'), usuario=request.POST.get('usuario'))

		return redirect('mostrarPrestamos')

	else:
		pk = request.POST.get('pk_prestamo')
		prestamo = Prestamo.objects.get(pk=pk)
		data = {'libro': prestamo.libro, 'fecha': prestamo.fecha, 'usuario': prestamo.usuario}
		form = PrestamoForm(data)
		context = {'login': user_activo, 'form': form , 'pk_prestamo' : pk}
		return render(request, 'modificarPrestamo.html', context)
