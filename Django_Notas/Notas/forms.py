from django.forms.widgets import *
from django import forms
from Notas.models import Cat_estatus


class CreateNewEstatusForm(forms.ModelForm):
	class Meta:
		model = Cat_estatus
		widgets = {
			"descripcion": TextInput(attrs={"class": "form-control", "": ""}),
		}
		exclude = ["fecha_creacion"]
