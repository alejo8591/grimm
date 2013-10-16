# -*- coding: utf-8 -*- 
from django.contrib import admin
from courses.models import Course, Faculty, AcademicProgram

class CourseAdmin(admin.ModelAdmin):
	fields = ('nameCourse', 'codeCourse', 'descriptionCourse', 'courseFaculty', 'courseAcademicProgram', 'dayCourse',)
	#exclude = ('createTime', 'updateTime', )

class FacultyAdmin(admin.ModelAdmin):
	fields = ('nameFaculty', 'codeFaculty', 'descriptionFaculty', )
	#exclude = ('createTime', 'updateTime', )

class AcademicProgramAdmin(admin.ModelAdmin):
	fields = ('nameAcademicProgram', 'codeAcademicProgram', 'descriptionAcademicProgram',)
	#exclude = ('createTime', 'updateTime', )


admin.site.register(Course, CourseAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(AcademicProgram, AcademicProgramAdmin)