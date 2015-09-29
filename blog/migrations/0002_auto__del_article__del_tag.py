# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

  def forwards(self, orm):
    # Deleting model 'Article'
    db.delete_table('blog_article')

    # Removing M2M table for field tags on 'Article'
    db.delete_table(db.shorten_name('blog_article_tags'))

    # Deleting model 'Tag'
    db.delete_table('blog_tag')


  def backwards(self, orm):
    # Adding model 'Article'
    db.create_table('blog_article', (
      ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
      ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.School'], blank=True, null=True)),
      ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('general_page', self.gf('django.db.models.fields.BooleanField')(default=False)),
      ('body', self.gf('django.db.models.fields.TextField')()),
      ('create_date', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
      ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
      ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
      ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
      ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Property'], blank=True, null=True)),
    ))
    db.send_create_signal('blog', ['Article'])

    # Adding M2M table for field tags on 'Article'
    m2m_table_name = db.shorten_name('blog_article_tags')
    db.create_table(m2m_table_name, (
      ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
      ('article', models.ForeignKey(orm['blog.article'], null=False)),
      ('tag', models.ForeignKey(orm['blog.tag'], null=False))
    ))
    db.create_unique(m2m_table_name, ['article_id', 'tag_id'])

    # Adding model 'Tag'
    db.create_table('blog_tag', (
      ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
    ))
    db.send_create_signal('blog', ['Tag'])


  models = {
    
  }

  complete_apps = ['blog']