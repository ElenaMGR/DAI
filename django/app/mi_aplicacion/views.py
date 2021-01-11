from django.shortcuts import render, HttpResponse, redirect
from .models import Libro, Autor, Prestamo
from .forms import LibroForm, AutorForm, PrestamoForm, PrestamoStaffForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

user_activo = ""

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
	context= {'login': user_activo, 'libros': libros, 'staff': request.user.is_staff}
	return render(request, 'libro.html', context)

def mostrarAutores (request):
	user_activo = request.user.username
	autores = Autor.objects.all()

	context= {'login': user_activo, 'autores': autores, 'staff': request.user.is_staff}
	return render(request, 'autor.html', context)

@login_required
def mostrarPrestamos (request):
	user_activo = request.user.username
	if request.user.is_staff:
		prestamos = Prestamo.objects.all()
	else:
		prestamos = Prestamo.objects.filter(usuario=request.user)

	context = {'login': user_activo, 'prestamos': prestamos}
	return render(request, 'prestamo.html', context)

@login_required
@permission_required('mi_aplicacion.libro.can_add_libro', login_url='mostrarLibros')
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

@login_required
@permission_required('mi_aplicacion.libro.can_delete_libro', login_url='mostrarLibros')
def eliminarLibro (request):
	Libro.objects.filter(pk=request.POST.get('pk_libro')).delete()
	return redirect('mostrarLibros')

@login_required
@permission_required('mi_aplicacion.libro.can_change_libro', login_url='mostrarLibros')
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

@login_required
@permission_required('mi_aplicacion.autor.can_add_autor', login_url='mostrarAutores')
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

@login_required
@permission_required('mi_aplicacion.autor.can_delete_autor', login_url='mostrarAutores')
def eliminarAutor (request):
	user_activo = request.user.username
	Autor.objects.filter(pk=request.POST.get('pk_autor')).delete()
	return redirect('mostrarAutores')

@login_required
@permission_required('mi_aplicacion.autor.can_change_autor', login_url='mostrarAutores')
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

@login_required
def addPrestamo (request):
	user_activo = request.user.username
	if request.method == 'POST':
		if request.user.is_staff:
			form = PrestamoStaffForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('mostrarPrestamos')
		else:
			form = PrestamoForm(request.POST)
			if form.is_valid():
				prestamo = form.save(commit=False)
				prestamo.usuario=request.user
				prestamo.save()
				return redirect('mostrarPrestamos')

	else:
		if request.user.is_staff:
			form = PrestamoStaffForm()
		else:
			form = PrestamoForm()

	context = {'login': user_activo, 'form': form , 'staff': request.user.is_staff}

	return render(request, 'addPrestamo.html', context)

@login_required
def eliminarPrestamo (request):
	user_activo = request.user.username
	Prestamo.objects.filter(pk=request.POST.get('pk_prestamo')).delete()
	return redirect('mostrarPrestamos')

@login_required
def modificarPrestamo (request):
	user_activo = request.user.username
	if request.method == 'POST' and 'modificado' in request.POST:
		if request.user.is_staff:
			usuario=request.POST.get('usuario')
		else: 
			usuario=request.user
		Prestamo.objects.filter(pk=request.POST.get('pk_prestamo')).update(libro=request.POST.get('libro'), fecha=request.POST.get('fecha'), usuario=usuario)
		return redirect('mostrarPrestamos')

	else:
		pk = request.POST.get('pk_prestamo')
		prestamo = Prestamo.objects.get(pk=pk)
		if request.user.is_staff:
			data = {'libro': prestamo.libro, 'fecha': prestamo.fecha, 'usuario': prestamo.usuario}
			form = PrestamoStaffForm(data)
		else:
			data = {'libro': prestamo.libro, 'fecha': prestamo.fecha}
			form = PrestamoForm(data)
		context = {'login': user_activo, 'form': form , 'pk_prestamo' : pk, 'staff': request.user.is_staff}
		return render(request, 'modificarPrestamo.html', context)

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()

		return redirect("login")
	else:
		form = RegisterForm()

	context = {'form': form }

	return render(response, "registration/register.html", context)
