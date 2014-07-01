# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PropertyLeaseTerm.activve'
        db.delete_column('main_propertyleaseterm', 'activve')

        # Adding field 'PropertyLeaseTerm.active'
        db.add_column('main_propertyleaseterm', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'PropertyLeaseStart.activve'
        db.delete_column('main_propertyleasestart', 'activve')

        # Adding field 'PropertyLeaseStart.active'
        db.add_column('main_propertyleasestart', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'PropertyLeaseType.activve'
        db.delete_column('main_propertyleasetype', 'activve')

        # Adding field 'PropertyLeaseType.active'
        db.add_column('main_propertyleasetype', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PropertyLeaseTerm.activve'
        db.add_column('main_propertyleaseterm', 'activve',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'PropertyLeaseTerm.active'
        db.delete_column('main_propertyleaseterm', 'active')

        # Adding field 'PropertyLeaseStart.activve'
        db.add_column('main_propertyleasestart', 'activve',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'PropertyLeaseStart.active'
        db.delete_column('main_propertyleasestart', 'active')

        # Adding field 'PropertyLeaseType.activve'
        db.add_column('main_propertyleasetype', 'activve',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'PropertyLeaseType.active'
        db.delete_column('main_propertyleasetype', 'active')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.amenity': {
            'Meta': {'object_name': 'Amenity', 'ordering': "['amenity']"},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '3'})
        },
        'main.article': {
            'Meta': {'object_name': 'Article', 'ordering': "['-create_date']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'general_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['main.School']"}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['main.Tag']", 'blank': 'True', 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.carepackage': {
            'Meta': {'object_name': 'CarePackage'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sent_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.deal': {
            'Meta': {'object_name': 'Deal', 'ordering': "['-sponsored', '-id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.event': {
            'Meta': {'object_name': 'Event', 'ordering': "['-sponsored', '-id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.property': {
            'Meta': {'object_name': 'Property', 'ordering': "['id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['main.Amenity']", 'blank': 'True', 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'blank': 'True', 'decimal_places': '6', 'max_digits': '12'}),
            'lease_start': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['main.PropertyLeaseStart']", 'blank': 'True', 'symmetrical': 'False'}),
            'lease_term': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['main.PropertyLeaseTerm']", 'blank': 'True', 'symmetrical': 'False'}),
            'lease_type': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['main.PropertyLeaseType']", 'blank': 'True', 'symmetrical': 'False'}),
            'long': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'blank': 'True', 'decimal_places': '6', 'max_digits': '12'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'special': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'MAIN'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['auth.User']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'main.propertyfavorite': {
            'Meta': {'object_name': 'PropertyFavorite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.propertyimage': {
            'Meta': {'object_name': 'PropertyImage', 'ordering': "['-main', 'order', 'caption']"},
            'caption': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"})
        },
        'main.propertyleasestart': {
            'Meta': {'object_name': 'PropertyLeaseStart'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_start': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.propertyleaseterm': {
            'Meta': {'object_name': 'PropertyLeaseTerm'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_term': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.propertyleasetype': {
            'Meta': {'object_name': 'PropertyLeaseType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.propertyreserve': {
            'Meta': {'object_name': 'PropertyReserve'},
            'agree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'evicted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'felony': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'floor_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.PropertyRoom']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'move_in_date': ('django.db.models.fields.DateField', [], {}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.propertyroom': {
            'Meta': {'object_name': 'PropertyRoom', 'ordering': "['price', 'bed_count']"},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bath_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.roommate': {
            'Meta': {'object_name': 'Roommate', 'ordering': "['-id']"},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['main.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'mascot': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.tag': {
            'Meta': {'object_name': 'Tag', 'ordering': "['tag_name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['main']