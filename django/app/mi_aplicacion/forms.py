from django import forms
from .models import Libro, Autor, Prestamo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro
		fields = ('titulo', 'autores',)

class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor
		fields = ('nombre', 'apellidos',)

class PrestamoForm(forms.ModelForm):
	class Meta:
		model = Prestamo
		fields = ('libro', 'fecha', 'usuario',)
		widgets = {
			'fecha': forms.DateInput(attrs={'type':'date'})
		}

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]