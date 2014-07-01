# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Roommate.property'
        db.add_column('main_roommate', 'property',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Event.date_time'
        db.delete_column('main_event', 'date_time')

        # Adding field 'Event.property'
        db.add_column('main_event', 'property',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.date'
        db.add_column('main_event', 'date',
                      self.gf('django.db.models.fields.DateField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Event.time'
        db.add_column('main_event', 'time',
                      self.gf('django.db.models.fields.TimeField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'Article.property'
        db.add_column('main_article', 'property',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Property'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Roommate.property'
        db.delete_column('main_roommate', 'property_id')


        # User chose to not deal with backwards NULL issues for 'Event.date_time'
        raise RuntimeError("Cannot reverse this migration. 'Event.date_time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.date_time'
        db.add_column('main_event', 'date_time',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Deleting field 'Event.property'
        db.delete_column('main_event', 'property_id')

        # Deleting field 'Event.date'
        db.delete_column('main_event', 'date')

        # Deleting field 'Event.time'
        db.delete_column('main_event', 'time')

        # Deleting field 'Article.property'
        db.delete_column('main_article', 'property_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.amenity': {
            'Meta': {'object_name': 'Amenity', 'ordering': "['amenity']"},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'})
        },
        'main.article': {
            'Meta': {'object_name': 'Article', 'ordering': "['-create_date']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'general_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']", 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']", 'null': 'True', 'blank': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'contact_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.deal': {
            'Meta': {'object_name': 'Deal', 'ordering': "['-sponsored', '-id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.event': {
            'Meta': {'object_name': 'Event', 'ordering': "['-sponsored', '-id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']", 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.TimeField', [], {'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.package': {
            'Meta': {'object_name': 'Package', 'ordering': "['-order']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Service']", 'null': 'True', 'blank': 'True'}),
            'similar_property_strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']", 'null': 'True', 'blank': 'True'}),
            'recurring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Service']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'main.property': {
            'Meta': {'object_name': 'Property', 'ordering': "['-top_list', '-sponsored', '-package__order', 'id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Amenity']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True', 'null': 'True'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '12', 'null': 'True', 'blank': 'True'}),
            'lease_term': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.PropertyLeaseTerm']", 'null': 'True', 'blank': 'True'}),
            'lease_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.PropertyLeaseType']", 'null': 'True', 'blank': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '12', 'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']", 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Service']", 'null': 'True', 'blank': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'top_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'APT'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'main.propertyfavorite': {
            'Meta': {'object_name': 'PropertyFavorite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.propertyimage': {
            'Meta': {'object_name': 'PropertyImage', 'ordering': "['-main', 'order', 'caption']"},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True', 'null': 'True'}),
            'floorplan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"})
        },
        'main.propertyleasestart': {
            'Meta': {'object_name': 'PropertyLeaseStart', 'ordering': "['order']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_start': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.propertyleaseterm': {
            'Meta': {'object_name': 'PropertyLeaseTerm', 'ordering': "['order']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_term': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lease_term_short': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True', 'null': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.propertyleasetype': {
            'Meta': {'object_name': 'PropertyLeaseType', 'ordering': "['lease_type']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.propertyreserve': {
            'Meta': {'object_name': 'PropertyReserve', 'ordering': "['-reserve_date']"},
            'agree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'evicted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'felony': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'floor_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.PropertyRoom']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'move_in_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'reserve_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'main.propertyroom': {
            'Meta': {'object_name': 'PropertyRoom', 'ordering': "['price', 'bed_count']"},
            'bath_count': ('django.db.models.fields.DecimalField', [], {'decimal_places': '1', 'max_digits': '5'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_start': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['main.PropertyLeaseStart']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.propertyschedule': {
            'Meta': {'object_name': 'PropertySchedule', 'ordering': "['-create_date']"},
            'create_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'schedule_date': ('django.db.models.fields.DateField', [], {}),
            'schedule_time': ('django.db.models.fields.TimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'main.propertyvideo': {
            'Meta': {'object_name': 'PropertyVideo', 'ordering': "['-main', 'order']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'main.roommate': {
            'Meta': {'object_name': 'Roommate', 'ordering': "['-id']"},
            'create_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']", 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.service': {
            'Meta': {'object_name': 'Service'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'R'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.tag': {
            'Meta': {'object_name': 'Tag', 'ordering': "['tag_name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'related_name': "'profile'"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']