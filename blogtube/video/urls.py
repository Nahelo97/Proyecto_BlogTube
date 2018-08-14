from django.conf.urls import url
from . import views
urlpatterns= [
 url(r"^$",views.vista_video,name='vista_video'),
 url(r"Comedia/$",views.comedia,name='comedia'),
 url(r"Terror/$",views.terror,name='terror'),
 url(r"Musica/$",views.musica,name='musica'),
 url(r"Gaming/$",views.gaming,name='gaming'),
 url(r"Conspiraciones/$",views.conspiraciones,name='conspiraciones')
 ]