# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('main_userprofile')

        # Adding model 'CustomUser'
        db.create_table('main_customuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('main', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name('main_customuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm['main.customuser'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name('main_customuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm['main.customuser'], null=False)),
            ('permission', models.ForeignKey(orm['auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])


        # Changing field 'Property.user'
        db.alter_column('main_property', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['main.CustomUser']))

        # Changing field 'PropertyFavorite.user'
        db.alter_column('main_propertyfavorite', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.CustomUser']))

        # Changing field 'PropertyReserve.user'
        db.alter_column('main_propertyreserve', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.CustomUser']))

        # Changing field 'Blog.user'
        db.alter_column('main_blog', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.CustomUser']))

    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('main_userprofile', (
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('main', ['UserProfile'])

        # Deleting model 'CustomUser'
        db.delete_table('main_customuser')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name('main_customuser_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name('main_customuser_user_permissions'))


        # Changing field 'Property.user'
        db.alter_column('main_property', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

        # Changing field 'PropertyFavorite.user'
        db.alter_column('main_propertyfavorite', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'PropertyReserve.user'
        db.alter_column('main_propertyreserve', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Blog.user'
        db.alter_column('main_blog', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
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
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['main.School']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.CustomUser']"})
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
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sent_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'symmetrical': 'False', 'to': "orm['main.Amenity']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'contact_first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'contact_last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fee_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'blank': 'True', 'decimal_places': '6', 'max_digits': '12'}),
            'long': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'blank': 'True', 'decimal_places': '6', 'max_digits': '12'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.School']"}),
            'special': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'MAIN'", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['main.CustomUser']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '300', 'blank': 'True'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'main.propertyfavorite': {
            'Meta': {'object_name': 'PropertyFavorite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.CustomUser']"})
        },
        'main.propertyimage': {
            'Meta': {'object_name': 'PropertyImage', 'ordering': "['-main', 'order', 'caption']"},
            'caption': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '40', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"})
        },
        'main.propertyreserve': {
            'Meta': {'object_name': 'PropertyReserve'},
            'agree': ('django.db.models.fields.BooleanField', [], {}),
            'credit': ('django.db.models.fields.BooleanField', [], {}),
            'evicted': ('django.db.models.fields.BooleanField', [], {}),
            'felony': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'floor_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.PropertyRoom']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'move_in_date': ('django.db.models.fields.DateField', [], {}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.CustomUser']"})
        },
        'main.propertyroom': {
            'Meta': {'object_name': 'PropertyRoom', 'ordering': "['price', 'bed_count']"},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bath_count': ('django.db.models.fields.DecimalField', [], {'decimal_places': '1', 'max_digits': '5'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Property']"}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'main.roommate': {
            'Meta': {'object_name': 'Roommate'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['main']