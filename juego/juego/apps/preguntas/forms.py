from models import Pregunta,Respuesta

from django.forms import ModelForm


class preguntaForm(ModelForm):
	class Meta:
		model = Pregunta




class RespuestaForm(ModelForm):
	class Meta:
		model = Respuesta