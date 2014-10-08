from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  Pregunta(models.Model):
	user=models.ForeignKey(User)
	pregunta=models.CharField(max_length='500',null=True)
	fecha=models.DateField(auto_now=True)
	def __unicode__(self):
		return "%s %s"%(self.pregunta)





