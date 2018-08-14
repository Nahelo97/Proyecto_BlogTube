# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Categoria(models.Model):
	nombre=models.CharField(max_length=200,verbose_name='Categoria',blank=False,null=True)
	def __str__(self):
		return u'%s' % (self.nombre)
	def __unicode__(self):
		return self.__str__()

class Video(models.Model):
	nombre=models.CharField(max_length=200,verbose_name='Nombre',blank=False,null=True)
	descripcion=models.TextField(verbose_name='Descripcion',blank=False,null=True)
	contenido = models.CharField(max_length=200,verbose_name='Contenido',blank=False,null=True)	
	categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT,blank=False,null=True)
	fecha = models.DateTimeField(auto_now=False,auto_now_add=False,verbose_name="Fecha",blank=False,null=True)
	imagen = models.ImageField(upload_to='media/',height_field=None, width_field=None, max_length=100,verbose_name="Imagen",blank=True,null=True)
	def __str__(self):
		return u'%s' % (self.nombre)
	def __unicode__(self):
		return self.__str__()

class Comentario(models.Model):
	usuario=models.CharField(max_length=200,verbose_name='Usuario',blank=False,null=True)
	mail=models.EmailField(max_length=200,verbose_name='Correo',blank=False,null=True)
	video=models.ForeignKey(Video,on_delete=models.PROTECT,blank=False,null=True)
	fecha=models.DateTimeField(auto_now=False,auto_now_add=False,verbose_name='Fecha',blank=False,null=True)
	comentario=models.TextField(verbose_name='Comentario',blank=False,null=True)
	def __str__(self):
		return u'%s' % (self.nombre)
	def __unicode__(self):
		return self.__str__()