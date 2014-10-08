from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('juego.apps.autenticacion.urls')),



    url(r'^user/login/$', 'juego.apps.autenticacion.views.loguet_in'),
    url(r'^salir/$', 'juego.apps.autenticacion.views.loguet_out'),

    url(r'^registrarse/$', 'juego.apps.usuario.views.Registro'),


 	url(r'^preguntas/$', 'juego.apps.preguntas.views.pregunta'),
	url(r'^respuestas/$', 'juego.apps.preguntas.views.respuesta'),

)
