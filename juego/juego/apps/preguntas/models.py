from django.db import models
from django.contrib.auth.models import User
from juego.apps.preguntas.models import *
# Create your models here.

class  Pregunta(models.Model):
	user=models.ForeignKey(User)
	pregunta=models.CharField(max_length='500',null=True)
	fecha=models.DateField(auto_now=True)
	def __unicode__(self):
		return "%s %s"%(self.pregunta)



class  Respuesta(models.Model):
	respuesta1=models.CharField(max_length='500',null=True)
	respuesta2=models.CharField(max_length='500',null=True)
	respuesta3=models.CharField(max_length='500',null=True)
	respuesta4=models.CharField(max_length='500',null=True)
	def __unicode__(self):
		return "%s %s"%(self.respuesta1)
