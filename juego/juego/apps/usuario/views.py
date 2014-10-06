from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms import UsuarioForm

# Create your views here.

def Registro(request):
  if request.method=='POST':
    formulario=UserCreationForm(request.POST)
    usuario=request.POST['username']
    if formulario.is_valid():
      formulario.save()
      return HttpResponseRedirect('/user/login/')
  else:
    formulario=UserCreationForm()
  return render_to_response('registrarse.html',{'registro':formulario},context_instance=RequestContext(request))