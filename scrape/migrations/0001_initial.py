# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table('scrape_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('scrape', ['Source'])

        # Adding model 'Apartment'
        db.create_table('scrape_apartment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Source'])),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_cd', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=15)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(decimal_places=6, max_digits=12)),
            ('long', self.gf('django.db.models.fields.DecimalField')(decimal_places=6, max_digits=12)),
            ('phone', self.gf('localflavor.us.models.PhoneNumberField')(null=True, blank=True, max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('exists', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('scrape', ['Apartment'])

        # Adding model 'ApartmentImage'
        db.create_table('scrape_apartmentimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Apartment'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('scrape', ['ApartmentImage'])

        # Adding model 'ApartmentFloorPlan'
        db.create_table('scrape_apartmentfloorplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Apartment'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(decimal_places=1, max_digits=5)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('scrape', ['ApartmentFloorPlan'])

        # Adding model 'AmenityCrossWalk'
        db.create_table('scrape_amenitycrosswalk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amenity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Amenity'])),
            ('scrape_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('scrape', ['AmenityCrossWalk'])

        # Adding model 'ApartmentAmenity'
        db.create_table('scrape_apartmentamenity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scrape.Apartment'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('scrape', ['ApartmentAmenity'])

        # Adding model 'Log'
        db.create_table('scrape_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.City'])),
            ('apartment_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(null=True, max_length=200)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 23, 0, 0))),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('comment', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=70)),
        ))
        db.send_create_signal('scrape', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Source'
        db.delete_table('scrape_source')

        # Deleting model 'Apartment'
        db.delete_table('scrape_apartment')

        # Deleting model 'ApartmentImage'
        db.delete_table('scrape_apartmentimage')

        # Deleting model 'ApartmentFloorPlan'
        db.delete_table('scrape_apartmentfloorplan')

        # Deleting model 'AmenityCrossWalk'
        db.delete_table('scrape_amenitycrosswalk')

        # Deleting model 'ApartmentAmenity'
        db.delete_table('scrape_apartmentamenity')

        # Deleting model 'Log'
        db.delete_table('scrape_log')


    models = {
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'multi_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'property.amenity': {
            'Meta': {'object_name': 'Amenity', 'ordering': "['amenity']"},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'})
        },
        'school.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['main.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
            'mascot': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scrape.amenitycrosswalk': {
            'Meta': {'object_name': 'AmenityCrossWalk'},
            'amenity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Amenity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scrape_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'scrape.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '12'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '12'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Source']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'})
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
            'bath_count': ('django.db.models.fields.DecimalField', [], {'decimal_places': '1', 'max_digits': '5'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'scrape.apartmentimage': {
            'Meta': {'object_name': 'ApartmentImage'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'scrape.log': {
            'Meta': {'object_name': 'Log', 'ordering': "['-datetime']"},
            'apartment_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']"}),
            'comment': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '70'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 23, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'scrape.source': {
            'Meta': {'object_name': 'Source'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['scrape']