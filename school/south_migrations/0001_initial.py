# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import school.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_user_type'),
        ('property', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('heading', models.CharField(null=True, max_length=200, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to=school.models.get_deal_image_path, blank=True)),
                ('property', models.ForeignKey(to='property.Property')),
            ],
            options={
                'ordering': ['-sponsored', '-id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('heading', models.CharField(null=True, max_length=200, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to=school.models.get_event_image_path, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('location', models.CharField(max_length=100)),
                ('property', models.ForeignKey(null=True, to='property.Property', blank=True)),
            ],
            options={
                'ordering': ['-sponsored', '-id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('long', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('link', models.CharField(null=True, max_length=100, blank=True)),
                ('mascot', models.CharField(null=True, max_length=50, blank=True)),
                ('long', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to=school.models.get_school_image_path)),
                ('city', models.ForeignKey(null=True, to='main.City', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='school',
            field=models.ForeignKey(to='school.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='school',
            field=models.ForeignKey(to='school.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deal',
            name='school',
            field=models.ForeignKey(to='school.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deal',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
