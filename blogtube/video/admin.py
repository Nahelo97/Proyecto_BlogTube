# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Video, Categoria, Comentario
# Register your models here.

admin.site.register(Video)
admin.site.register(Categoria)
admin.site.register(Comentario)
