# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Task'
        db.delete_table('flowtask_task')

        # Adding model 'TaskNew'
        db.create_table('flowtask_tasknew', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='BUG', max_length=3)),
            ('urgency', self.gf('django.db.models.fields.CharField')(default='4', max_length=3)),
            ('status', self.gf('django.db.models.fields.CharField')(default='SUB', max_length=3)),
        ))
        db.send_create_signal('flowtask', ['TaskNew'])


    def backwards(self, orm):
        # Adding model 'Task'
        db.create_table('flowtask_task', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('flowtask', ['Task'])

        # Deleting model 'TaskNew'
        db.delete_table('flowtask_tasknew')


    models = {
        'flowtask.tasknew': {
            'Meta': {'object_name': 'TaskNew'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'SUB'", 'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'BUG'", 'max_length': '3'}),
            'urgency': ('django.db.models.fields.CharField', [], {'default': "'4'", 'max_length': '3'})
        }
    }

    complete_apps = ['flowtask']