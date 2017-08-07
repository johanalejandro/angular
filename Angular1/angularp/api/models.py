# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Plato(models.Model):
	idP=models.IntegerField()
	titulo=models.CharField(max_length=30)
	tipo=models.CharField(max_length=30)
	precio=models.FloatField()
	cantidad=models.IntegerField()
	distancia=models.FloatField()
	valorNutricional=models.FloatField()
	imagen=models.CharField(max_length=300)
	valoracion=models.IntegerField()