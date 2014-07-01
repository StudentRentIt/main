# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PropertyRooms'
        db.create_table('main_propertyrooms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Rooms', to=orm['main.Property'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('bath_count', self.gf('django.db.models.fields.DecimalField')(decimal_places=1, max_digits=3)),
            ('sq_ft', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('main', ['PropertyRooms'])

        # Deleting field 'Property.bath_count'
        db.delete_column('main_property', 'bath_count')

        # Deleting field 'Property.price'
        db.delete_column('main_property', 'price')

        # Deleting field 'Property.sq_ft'
        db.delete_column('main_property', 'sq_ft')

        # Deleting field 'Property.image'
        db.delete_column('main_property', 'image')

        # Deleting field 'Property.bed_count'
        db.delete_column('main_property', 'bed_count')


        # Changing field 'Property.contact_first_name'
        db.alter_column('main_property', 'contact_first_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))

        # Changing field 'Property.contact_email'
        db.alter_column('main_property', 'contact_email', self.gf('django.db.models.fields.EmailField')(null=True, max_length=75))

        # Changing field 'Property.contact_phone'
        db.alter_column('main_property', 'contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(null=True, max_length=20))

        # Changing field 'Property.contact_last_name'
        db.alter_column('main_property', 'contact_last_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))
        # Adding field 'PropertyImage.caption'
        db.add_column('main_propertyimage', 'caption',
                      self.gf('django.db.models.fields.CharField')(default=True, blank=True, max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'PropertyRooms'
        db.delete_table('main_propertyrooms')


        # User chose to not deal with backwards NULL issues for 'Property.bath_count'
        raise RuntimeError("Cannot reverse this migration. 'Property.bath_count' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Property.bath_count'
        db.add_column('main_property', 'bath_count',
                      self.gf('django.db.models.fields.DecimalField')(decimal_places=1, max_digits=3),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Property.price'
        raise RuntimeError("Cannot reverse this migration. 'Property.price' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Property.price'
        db.add_column('main_property', 'price',
                      self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8),
                      keep_default=False)

        # Adding field 'Property.sq_ft'
        db.add_column('main_property', 'sq_ft',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Property.image'
        db.add_column('main_property', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Property.bed_count'
        raise RuntimeError("Cannot reverse this migration. 'Property.bed_count' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Property.bed_count'
        db.add_column('main_property', 'bed_count',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Property.contact_first_name'
        raise RuntimeError("Cannot reverse this migration. 'Property.contact_first_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Property.contact_first_name'
        db.alter_column('main_property', 'contact_first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'Property.contact_email'
        raise RuntimeError("Cannot reverse this migration. 'Property.contact_email' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Property.contact_email'
        db.alter_column('main_property', 'contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # User chose to not deal with backwards NULL issues for 'Property.contact_phone'
        raise RuntimeError("Cannot reverse this migration. 'Property.contact_phone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Property.contact_phone'
        db.alter_column('main_property', 'contact_phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Property.contact_last_name'
        raise RuntimeError("Cannot reverse this migration. 'Property.contact_last_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Property.contact_last_name'
        db.alter_column('main_property', 'contact_last_name', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Deleting field 'PropertyImage.caption'
        db.delete_column('main_propertyimage', 'caption')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.amenity': {
            'Meta': {'object_name': 'Amenity', 'ordering': "['amenity']"},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.blog': {
            'Meta': {'object_name': 'Blog', 'ordering': "['-create_date']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.carepackage': {
            'Meta': {'object_name': 'CarePackage'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'main.faq': {
            'Meta': {'object_name': 'FAQ', 'ordering': "['order']"},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.property': {
            'Meta': {'object_name': 'Property', 'ordering': "['id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Amenity']", 'null': 'True'}),
            'available_on': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'blank': 'True', 'max_digits': '12', 'null': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'blank': 'True', 'max_digits': '12', 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'MAIN'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '300'})
        },
        'main.propertyimage': {
            'Meta': {'object_name': 'PropertyImage'},
            'caption': ('django.db.models.fields.CharField', [], {'default': 'True', 'blank': 'True', 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Images'", 'to': "orm['main.Property']"})
        },
        'main.propertyrooms': {
            'Meta': {'object_name': 'PropertyRooms'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bath_count': ('django.db.models.fields.DecimalField', [], {'decimal_places': '1', 'max_digits': '3'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Rooms'", 'to': "orm['main.Property']"}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'main.roommate': {
            'Meta': {'object_name': 'Roommate'},
            'create_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"})
        },
        'main.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '3', 'max_digits': '8'}),
            'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '3', 'max_digits': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['main']