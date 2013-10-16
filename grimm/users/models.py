# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	user = models.OneToOneField(User)
	code = models.IntegerField(max_length=24, blank=False, null=False, unique=True, help_text="Ingrese su Código estudiantil, solo números", verbose_name="Código Estudiantil")
	
	class Meta:
		verbose_name = 'Estudiante'
     	#user = models.OneToOneField(User)
        #code = models.IntegerField(max_length=24)
        verbose_name_plural = 'Estudiantes'
        #user = models.OneToOneField(User)
        #code = models.IntegerField(max_length=24)
    
    	def __unicode__(self):
    		pass
