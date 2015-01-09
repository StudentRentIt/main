# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import school.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('heading', models.CharField(max_length=200, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, blank=True, upload_to=school.models.get_deal_image_path)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('heading', models.CharField(max_length=200, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, blank=True, upload_to=school.models.get_event_image_path)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('location', models.CharField(max_length=100)),
                ('property', models.ForeignKey(to='property.Property', blank=True, null=True)),
            ],
            options={
                'ordering': ['-sponsored', '-id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lat', models.DecimalField(max_digits=10, decimal_places=6)),
                ('long', models.DecimalField(max_digits=10, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100, null=True, blank=True)),
                ('mascot', models.CharField(max_length=50, null=True, blank=True)),
                ('long', models.DecimalField(max_digits=10, decimal_places=6)),
                ('lat', models.DecimalField(max_digits=10, decimal_places=6)),
                ('image', models.ImageField(null=True, upload_to=school.models.get_school_image_path)),
                ('city', models.ForeignKey(to='main.City', blank=True, null=True)),
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
