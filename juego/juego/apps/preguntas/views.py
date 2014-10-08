from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from models import Pregunta
from forms import preguntaForm
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