from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms import *

# Create your views here.

def Registro(request):
  if request.method=='POST':
    formulario=fusuario(request.POST)
    tipou=request.POST['stipo']
    usuario=request.POST['username']
    if formulario.is_valid():
      formulario.save()
      u=User.objects.get(username=usuario)
      if tipou[0] == '1':
        u.is_superuser=True
        if tipou[1] == '1':
          u.is_staff=True
        else:
          u.is_staff=False
      else:
        u.is_staff=True
        if tipou[1] == '1':
          u.is_staff=True
        else:
          u.is_staff=False
      u.save()
      return HttpResponseRedirect('/user/login/')
  else:
    formulario=fusuario()
  return render_to_response('registrarse.html',{'registro':formulario},context_instance=RequestContext(request))

