# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0003_auto_20150109_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True, blank=True, editable=False)),
                ('contact', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('default_school', models.ForeignKey(null=True, to='school.School', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
