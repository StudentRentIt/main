# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

  def forwards(self, orm):
    # Adding model 'Tag'
    db.rename_table('main_tag', 'blog_tag')

    # Adding model 'Article'
    db.rename_table('main_article', 'blog_article')


  def backwards(self, orm):
    # Removing model 'Tag'
    db.rename_table('blog_tag', 'main_tag')

    # Removing model 'Article'
    db.rename_table('blog_article', 'main_article')
