# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Property'
        db.delete_table(u'main_property')

        # Removing M2M table for field amenities on 'Property'
        db.delete_table(db.shorten_name(u'main_property_amenities'))

        # Deleting model 'PropertyImage'
        db.delete_table(u'main_propertyimage')


    def backwards(self, orm):
        # Adding model 'Property'
        db.create_table(u'main_property', (
            ('fee_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('special', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('type', self.gf('django.db.models.fields.CharField')(default='MAIN', max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('available_on', self.gf('django.db.models.fields.DateField')(null=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.University'])),
        ))
        db.send_create_signal(u'main', ['Property'])

        # Adding M2M table for field amenities on 'Property'
        m2m_table_name = db.shorten_name(u'main_property_amenities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm[u'main.property'], null=False)),
            ('amenity', models.ForeignKey(orm[u'main.amenity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'amenity_id'])

        # Adding model 'PropertyImage'
        db.create_table(u'main_propertyimage', (
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['main.Property'])),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main', ['PropertyImage'])


    models = {
        u'main.amenity': {
            'Meta': {'ordering': "['amenity']", 'object_name': 'Amenity'},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.university': {
            'Meta': {'object_name': 'University'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']