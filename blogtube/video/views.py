# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from .models import Video, Categoria, Comentario
def vista_video(request):
	template='video/videos.html'
	data= dict()
	data['titulo']='Video del Día'
	data['vista_video']=Video.objects.all()
	data['categs']=Categoria.objects.all()
	return render(request,template,data)
def comedia(request):
	template='video/Comedia.html'
	data=dict()
	data['comedia']=Video.objects.filter(categoria__nombre="Comedia")
	return render(request,template,data)
def terror(request):
	template='video/Terror.html'
	data=dict()
	data['terror']=Video.objects.filter(categoria__nombre='Terror')
	return render(request,template,data)
def musica(request):
	template='video/Musica.html'
	data=dict()
	data['musica']=Video.objects.filter(categoria__nombre='Musica')
	return render(request,template,data)
def gaming(request):
	template='video/Gaming.html'
	data=dict()
	data['gaming']=Video.objects.filter(categoria__nombre='gaming')
	return render(request,template,data)
def conspiraciones(request):
	template='video/Conspiraciones.html'
	data=dict()
	data['conspiraciones']=Video.objects.filter(categoria__nombre='Conspiraciones')
	return render(request,template,data)