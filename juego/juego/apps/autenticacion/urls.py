from django.conf.urls import patterns, include, url
from .views import index
urlpatterns = patterns('',
 	#url(r'^$','django.contrib.auth.views.login',{'template_name':'index.html'},name='login'),

 	#url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
 	#url(r'^registrarse/$',Registrarse.as_view(),name='registrarse')
 	url(r'^$',index),

)
