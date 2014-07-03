# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ApartmentAmenity.title'
        db.alter_column('scrape_apartmentamenity', 'title', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'ApartmentAmenity.title'
        db.alter_column('scrape_apartmentamenity', 'title', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'main.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.City']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'mascot': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scrape.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '80', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'source_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'})
        },
        'scrape.apartmentamenity': {
            'Meta': {'object_name': 'ApartmentAmenity'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
        'scrape.scrapelog': {
            'Meta': {'object_name': 'ScrapeLog'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']"}),
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['scrape']