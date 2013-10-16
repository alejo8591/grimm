# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):

	TYPE_PERSON = (
		('Profesor', 'Profesor'),
		('Estudiante', 'Estudiante'),
	)
	user = models.OneToOneField(User)
	code = models.CharField(max_length=24, blank=False, null=False, unique=True, help_text="Ingrese su Código estudiantil, solo números", verbose_name="Código Estudiantil")
	profession = models.CharField(max_length=24, blank=False, null=False, unique=True, help_text="Ingrese la profesión de la persona", verbose_name="Profesión")
	typePersonProfile = models.CharField(max_length=24, choices=TYPE_PERSON, blank=False, null=False, help_text="Escoja el tipo de perfil de la persona", verbose_name="Tipo de Perfil")
	
	class Meta:
		verbose_name = 'Estudiante o Profesor'
        verbose_name_plural = 'Estudiantes o Profesores'
    
    	def __unicode__(self):
    		pass