# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

  def forwards(self, orm):
    # Adding M2M table for field tags on 'Article'
    m2m_table_name = db.shorten_name('blog_article_tags')
    db.create_table(m2m_table_name, (
      ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
      ('article', models.ForeignKey(orm['blog.article'], null=False)),
      ('tag', models.ForeignKey(orm['blog.tag'], null=False))
    ))
    db.create_unique(m2m_table_name, ['article_id', 'tag_id'])


  def backwards(self, orm):
    # Removing M2M table for field tags on 'Article'
    db.delete_table(db.shorten_name('blog_article_tags'))


  models = {
    'auth.group': {
      'Meta': {'object_name': 'Group'},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
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
      'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
      'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
      'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
      'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
      'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
      'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
      'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
    },
    'blog.article': {
      'Meta': {'object_name': 'Article', 'ordering': "['-create_date']"},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'body': ('django.db.models.fields.TextField', [], {}),
      'create_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
      'general_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
      'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Property']", 'null': 'True', 'blank': 'True'}),
      'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']", 'null': 'True', 'blank': 'True'}),
      'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.Tag']", 'null': 'True', 'blank': 'True'}),
      'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
    },
    'blog.tag': {
      'Meta': {'object_name': 'Tag', 'ordering': "['tag_name']"},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
    },
    'contenttypes.contenttype': {
      'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
      'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
    },
    'main.city': {
      'Meta': {'object_name': 'City'},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
      'multi_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
      'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
    },
    'property.amenity': {
      'Meta': {'object_name': 'Amenity', 'ordering': "['amenity']"},
      'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
      'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
      'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True', 'null': 'True'})
    },
    'property.package': {
      'Meta': {'object_name': 'Package', 'ordering': "['-order']"},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'description': ('django.db.models.fields.TextField', [], {}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
      'price': ('django.db.models.fields.IntegerField', [], {}),
      'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['property.Service']", 'null': 'True', 'blank': 'True'}),
      'similar_property_strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
      'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
    },
    'property.property': {
      'Meta': {'object_name': 'Property', 'ordering': "['-top_list', '-sponsored', '-package__order', 'id']"},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'addr': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
      'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['property.Amenity']", 'null': 'True', 'blank': 'True'}),
      'city': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
      'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True', 'null': 'True'}),
      'contact_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
      'contact_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
      'contact_phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
      'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
      'fee_desc': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '12', 'null': 'True', 'blank': 'True'}),
      'lease_term': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['property.PropertyLeaseTerm']", 'null': 'True', 'blank': 'True'}),
      'lease_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['property.PropertyLeaseType']", 'null': 'True', 'blank': 'True'}),
      'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '12', 'null': 'True', 'blank': 'True'}),
      'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Package']", 'null': 'True', 'blank': 'True'}),
      'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
      'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['property.Service']", 'null': 'True', 'blank': 'True'}),
      'special': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
      'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
      'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'top_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'type': ('django.db.models.fields.CharField', [], {'default': "'APT'", 'max_length': '20'}),
      'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
      'zip_cd': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True', 'null': 'True'})
    },
    'property.propertyleaseterm': {
      'Meta': {'object_name': 'PropertyLeaseTerm', 'ordering': "['order']"},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'lease_term': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
      'lease_term_short': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True', 'null': 'True'}),
      'order': ('django.db.models.fields.IntegerField', [], {})
    },
    'property.propertyleasetype': {
      'Meta': {'object_name': 'PropertyLeaseType', 'ordering': "['lease_type']"},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'lease_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
    },
    'property.service': {
      'Meta': {'object_name': 'Service'},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'description': ('django.db.models.fields.TextField', [], {}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'price': ('django.db.models.fields.IntegerField', [], {}),
      'service_type': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'}),
      'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
    },
    'school.school': {
      'Meta': {'object_name': 'School'},
      'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']", 'null': 'True', 'blank': 'True'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
      'lat': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
      'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
      'long': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '10'}),
      'mascot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
    }
  }

  complete_apps = ['blog']