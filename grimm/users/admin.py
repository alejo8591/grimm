# -*- coding: utf-8 -*- 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import Student

class UserInline(admin.StackedInline):
	model = Student
	can_delete = False
	verbose_name=u'Código del Estudiante'
	verbose_name_plural = u'estudiante'

class UserAdmin(UserAdmin):
	inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)