# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Apartment'
        db.create_table('scrape_apartment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('zip_cd', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('scrape', ['Apartment'])

        # Adding model 'ApartmentFeatures'
        db.create_table('scrape_apartmentfeatures', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Apartment'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('scrape', ['ApartmentFeatures'])

        # Adding model 'ApartmentFloorPlan'
        db.create_table('scrape_apartmentfloorplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Apartment'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('scrape', ['ApartmentFloorPlan'])

        # Adding model 'ScrapeLog'
        db.create_table('scrape_scrapelog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.City'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('scrape', ['ScrapeLog'])

        # Adding model 'ApartmentPic'
        db.create_table('scrape_apartmentpic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Apartment'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('scrape', ['ApartmentPic'])


    def backwards(self, orm):
        # Deleting model 'Apartment'
        db.delete_table('scrape_apartment')

        # Deleting model 'ApartmentFeatures'
        db.delete_table('scrape_apartmentfeatures')

        # Deleting model 'ApartmentFloorPlan'
        db.delete_table('scrape_apartmentfloorplan')

        # Deleting model 'ScrapeLog'
        db.delete_table('scrape_scrapelog')

        # Deleting model 'ApartmentPic'
        db.delete_table('scrape_apartmentpic')


    models = {
        'scrape.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'scrape.apartmentfeatures': {
            'Meta': {'object_name': 'ApartmentFeatures'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'scrape.apartmentfloorplan': {
            'Meta': {'object_name': 'ApartmentFloorPlan'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'bath_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'scrape.apartmentpic': {
            'Meta': {'object_name': 'ApartmentPic'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'scrape.city': {
            'Meta': {'object_name': 'City'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_cd': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'scrape.scrapelog': {
            'Meta': {'object_name': 'ScrapeLog'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.City']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['scrape']