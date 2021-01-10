from django import forms
from .models import Libro, Autor, Prestamo


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