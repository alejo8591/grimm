# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Faculty'
        db.create_table(u'courses_faculty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nameFaculty', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('codeFaculty', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('descriptionFaculty', self.gf('django.db.models.fields.TextField')()),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updateTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'courses', ['Faculty'])

        # Adding model 'AcademicProgram'
        db.create_table(u'courses_academicprogram', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nameAcademicProgram', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('codeAcademicProgram', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('descriptionAcademicProgram', self.gf('django.db.models.fields.TextField')()),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updateTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'courses', ['AcademicProgram'])

        # Adding model 'Course'
        db.create_table(u'courses_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nameCourse', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('codeCourse', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24)),
            ('descriptionCourse', self.gf('django.db.models.fields.TextField')()),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updateTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('courseFaculty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Faculty'])),
            ('courseAcademicProgram', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.AcademicProgram'])),
            ('dayCourse', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'courses', ['Course'])


    def backwards(self, orm):
        # Deleting model 'Faculty'
        db.delete_table(u'courses_faculty')

        # Deleting model 'AcademicProgram'
        db.delete_table(u'courses_academicprogram')

        # Deleting model 'Course'
        db.delete_table(u'courses_course')


    models = {
        u'courses.academicprogram': {
            'Meta': {'object_name': 'AcademicProgram'},
            'codeAcademicProgram': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'}),
            'createTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'descriptionAcademicProgram': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameAcademicProgram': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updateTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            'codeCourse': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'}),
            'courseAcademicProgram': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.AcademicProgram']"}),
            'courseFaculty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Faculty']"}),
            'createTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dayCourse': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'descriptionCourse': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameCourse': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updateTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'courses.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'codeFaculty': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24'}),
            'createTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'descriptionFaculty': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameFaculty': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updateTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['courses']