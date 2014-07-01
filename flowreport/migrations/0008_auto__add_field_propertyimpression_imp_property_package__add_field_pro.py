# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PropertyImpression.imp_property_package'
        db.add_column('flowreport_propertyimpression', 'imp_property_package',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['main.Package'], null=True),
                      keep_default=False)

        # Adding field 'PropertyImpression.imp_property_sponsored'
        db.add_column('flowreport_propertyimpression', 'imp_property_sponsored',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PropertyImpression.imp_property_package'
        db.delete_column('flowreport_propertyimpression', 'imp_property_package_id')

        # Deleting field 'PropertyImpression.imp_property_sponsored'
        db.delete_column('flowreport_propertyimpression', 'imp_property_sponsored')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flowreport.audience': {
            'Meta': {'object_name': 'Audience'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'flowreport.propertyimpression': {
            'Meta': {'ordering': "['-imp_date', 'property__title']", 'object_name': 'PropertyImpression'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'imp_property_package': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.Package']", 'null': 'True'}),
            'imp_property_sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'imp_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"})
        },
        'flowreport.report': {
            'Meta': {'object_name': 'Report'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audience': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['flowreport.Audience']", 'null': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'flowreport.schoolitemimpression': {
            'Meta': {'ordering': "['-imp_date']", 'object_name': 'SchoolItemImpression'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'imp_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'flowreport.schoolsearch': {
            'Meta': {'object_name': 'SchoolSearch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'search_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'main.amenity': {
            'Meta': {'ordering': "['amenity']", 'object_name': 'Amenity'},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'})
        },
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'main.package': {
            'Meta': {'ordering': "['-order']", 'object_name': 'Package'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['main.Service']", 'null': 'True'}),
            'similar_property_strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.property': {
            'Meta': {'ordering': "['-top_list', '-sponsored', '-package__order']", 'object_name': 'Property'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['main.Amenity']", 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'blank': 'True', 'decimal_places': '6', 'null': 'True'}),
            'lease_term': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['main.PropertyLeaseTerm']", 'null': 'True'}),
            'lease_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['main.PropertyLeaseType']", 'null': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'blank': 'True', 'decimal_places': '6', 'null': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.Package']", 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['main.Service']", 'null': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'top_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'APT'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '300'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'main.propertyleaseterm': {
            'Meta': {'ordering': "['order']", 'object_name': 'PropertyLeaseTerm'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_term': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lease_term_short': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '5'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.propertyleasetype': {
            'Meta': {'ordering': "['lease_type']", 'object_name': 'PropertyLeaseType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['main.City']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'mascot': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.service': {
            'Meta': {'object_name': 'Service'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flowreport']