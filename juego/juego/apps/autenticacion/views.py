from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AdminPasswordChangeForm, AuthenticationForm, authenticate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
  return render_to_response("index.html",{},RequestContext(request))

def loguet_in(request):
    if not request.user.is_anonymous():
         return render_to_response('user/privado.html', context_instance=RequestContext(request))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        ##if acceso.is_superuser:
                          #  return HttpResponseRedirect('/administrador')
                        #else:
                         #   return HttpResponseRedirect('/private')
                         return render_to_response('user/privado.html', context_instance=RequestContext(request))
                else:
                    return render_to_response('user/noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('user/nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('user/user_login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def loguet_out(request):
    logout(request)
    return HttpResponseRedirect('/')
