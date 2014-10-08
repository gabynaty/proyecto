from models import Pregunta

from django.forms import ModelForm


class preguntaForm(ModelForm):
	class Meta:
		model = Pregunta