from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from models import Pregunta,Respuesta
from forms import preguntaForm,RespuestaForm
# Create your views here.


def pregunta(request):
	if request.method=="POST":
		form=preguntaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/user/login/')
	else:
		form=preguntaForm()
	return render_to_response('pregunta.html',{'pregunta':form},context_instance = RequestContext(request))





def respuesta(request):
	if request.method=="POST":
		form=RespuestaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/user/login/')
	else:
		form=RespuestaForm()
	return render_to_response('respuesta.html',{'respuesta':form},context_instance = RequestContext(request))