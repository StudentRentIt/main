# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Amenity'
        db.create_table(u'main_amenity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amenity', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['Amenity'])

        # Adding model 'University'
        db.create_table(u'main_university', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('long', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'main', ['University'])

        # Adding model 'Property'
        db.create_table(u'main_property', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.University'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('postal_cd', self.gf('localflavor.us.models.USPostalCodeField')(max_length=2)),
            ('type', self.gf('django.db.models.fields.CharField')(default='MAIN', max_length=20)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('special', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fee_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('available_on', self.gf('django.db.models.fields.DateField')(null=True)),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('contact_first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact_last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
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
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['main.Property'])),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['PropertyImage'])


    def backwards(self, orm):
        # Deleting model 'Amenity'
        db.delete_table(u'main_amenity')

        # Deleting model 'University'
        db.delete_table(u'main_university')

        # Deleting model 'Property'
        db.delete_table(u'main_property')

        # Removing M2M table for field amenities on 'Property'
        db.delete_table(db.shorten_name(u'main_property_amenities'))

        # Deleting model 'PropertyImage'
        db.delete_table(u'main_propertyimage')


    models = {
        u'main.amenity': {
            'Meta': {'ordering': "['amenity']", 'object_name': 'Amenity'},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.property': {
            'Meta': {'ordering': "['id']", 'object_name': 'Property'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Amenity']", 'symmetrical': 'False'}),
            'available_on': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'bath_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_cd': ('localflavor.us.models.USPostalCodeField', [], {'max_length': '2'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'special': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'MAIN'", 'max_length': '20'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.University']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'main.propertyimage': {
            'Meta': {'object_name': 'PropertyImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['main.Property']"})
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