# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Apartment.address'
        db.alter_column('scrape_apartment', 'address', self.gf('django.db.models.fields.CharField')(max_length=80, null=True))

        # Changing field 'Apartment.phone'
        db.alter_column('scrape_apartment', 'phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True))

        # Changing field 'Apartment.description'
        db.alter_column('scrape_apartment', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Apartment.zip_cd'
        db.alter_column('scrape_apartment', 'zip_cd', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Apartment.address'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.address' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Apartment.address'
        db.alter_column('scrape_apartment', 'address', self.gf('django.db.models.fields.CharField')(max_length=80))

        # User chose to not deal with backwards NULL issues for 'Apartment.phone'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.phone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Apartment.phone'
        db.alter_column('scrape_apartment', 'phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Apartment.description'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Apartment.description'
        db.alter_column('scrape_apartment', 'description', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Apartment.zip_cd'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.zip_cd' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Apartment.zip_cd'
        db.alter_column('scrape_apartment', 'zip_cd', self.gf('django.db.models.fields.CharField')(max_length=15))

    models = {
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'main.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['main.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scrape.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
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
            'bath_count': ('django.db.models.fields.DecimalField', [], {'decimal_places': '1', 'max_digits': '5'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['scrape']