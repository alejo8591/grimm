# -*- coding: utf-8 -*- 
from django.db import models
from users.models import Person


class Faculty(models.Model):
	nameFaculty = models.CharField(max_length=256,  blank=False, null=False, help_text="Ingrese el nombre de la facultad", verbose_name="Nombre de la Facultad")
	codeFaculty = models.CharField(max_length=24, blank=False, null=False, unique=True, help_text="Ingrese el Código de identificación de la facultad", verbose_name="Código de la facultad")
	descriptionFaculty = models.TextField(help_text="Ingrese la Descripción de la facultad", verbose_name="Descripción de la facultad")
	#createUserId = models.ForeignKey(Person)
	createTime = models.DateTimeField(auto_now=True)
	#updateUserId = models.ForeignKey(Person)
	updateTime = models.DateTimeField(auto_now=True)
	
class AcademicProgram(models.Model):
	nameAcademicProgram = models.CharField(max_length=256,  blank=False, null=False, help_text="Ingrese el nombre del Programa Acádemico", verbose_name="Programa Acádemico")
	codeAcademicProgram = models.CharField(max_length=24, blank=False, null=False, unique=True, help_text="Ingrese el Código de identificación del programa academico", verbose_name="Código del programa")
	descriptionAcademicProgram = models.TextField(help_text="Ingrese la Descripción del programa academico", verbose_name="Descripción del Programa")
	#createUserId = models.ForeignKey(Person)
	createTime = models.DateTimeField(auto_now=True)
	#updateUserId = models.ForeignKey(Person)
	updateTime = models.DateTimeField(auto_now=True)
	
class Course(models.Model):
	DAYS = (
		('Lunes', 'Lunes'),
		('Martes', 'Martes'),
		('Miércoles', 'Miércoles'),
		('Jueves', 'Jueves'),
		('Viernes', 'Viernes'),
		('Sábado', 'Sábado'),
		('Domingo', 'Domingo'),
	)
	nameCourse = models.CharField(max_length=256, blank=False, null=False, help_text="Ingrese el nombre del Curso", verbose_name="Nombre del Curso")
	codeCourse = models.CharField(max_length=24, blank=False, null=False, unique=True, help_text="Ingrese el Código de identificación del curso", verbose_name="Código del Curso")
	descriptionCourse = models.TextField(help_text="Ingrese la Descripción del curso", verbose_name="Descripción del curso")
	#createUserId = models.ForeignKey(Person)
	createTime = models.DateTimeField(auto_now=True)
	#updateUserId = models.ForeignKey(Person)
	updateTime = models.DateTimeField(auto_now=True)
	courseFaculty = models.ForeignKey(Faculty, blank=False, null=False, help_text="Escoja la Facultad a la que pertence el Curso", verbose_name="Facultad")
	courseAcademicProgram = models.ForeignKey(AcademicProgram, blank=False, null=False, help_text="Escoja el Programa Acádemico al que pertence el Curso", verbose_name="Programa Acádemico")
	dayCourse = models.CharField(max_length=128, choices=DAYS, blank=False, null=False, help_text="Escoja el día que se lleva a cabo el Curso", verbose_name="Día del Curso")
