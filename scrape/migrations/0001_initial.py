# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table('scrape_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state_cd', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('scrape', ['City'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table('scrape_city')


    models = {
        'scrape.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_cd': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['scrape']