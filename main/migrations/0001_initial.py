# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import django.core.validators
import localflavor.us.models
import main.models


class Migration(migrations.Migration):

  dependencies = [
    ('property', '__first__'),
    ('auth', '0001_initial'),
  ]

  operations = [
    migrations.CreateModel(
      name='User',
      fields=[
        ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
        ('password', models.CharField(verbose_name='password', max_length=128)),
        ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
        ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
        ('username', models.CharField(unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, verbose_name='username')),
        ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
        ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
        ('email', models.EmailField(blank=True, verbose_name='email address', max_length=75)),
        ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
        ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
        ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
        ('groups', models.ManyToManyField(blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', verbose_name='groups', related_query_name='user')),
        ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', related_query_name='user')),
      ],
      options={
        'db_table': 'auth_user',
      },
      bases=(models.Model,),
    ),
    migrations.CreateModel(
      name='City',
      fields=[
        ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
        ('name', models.CharField(max_length=40)),
        ('state', localflavor.us.models.USStateField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
        ('link', models.CharField(blank=True, null=True, max_length=100)),
        ('multi_university', models.BooleanField(default=False)),
      ],
      options={
      },
      bases=(models.Model,),
    ),
    migrations.CreateModel(
      name='Contact',
      fields=[
        ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
        ('first_name', models.CharField(max_length=50)),
        ('last_name', models.CharField(max_length=50)),
        ('email', models.EmailField(max_length=75)),
        ('phone_number', localflavor.us.models.PhoneNumberField(null=True, max_length=20)),
        ('subject', models.CharField(max_length=100)),
        ('body', models.CharField(max_length=500)),
        ('contact_date', models.DateField(auto_now_add=True)),
        ('property', models.ForeignKey(blank=True, null=True, to='property.Property')),
      ],
      options={
      },
      bases=(models.Model,),
    ),
    migrations.CreateModel(
      name='Payment',
      fields=[
        ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
        ('payment_date', models.DateField(auto_now_add=True)),
        ('recurring', models.BooleanField(default=False)),
        ('amount', models.IntegerField()),
        ('property', models.ForeignKey(blank=True, null=True, to='property.Property')),
        ('services', models.ManyToManyField(blank=True, null=True, to='property.Service')),
        ('user', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
      ],
      options={
      },
      bases=(models.Model,),
    ),
    migrations.CreateModel(
      name='TeamMember',
      fields=[
        ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
        ('name', models.CharField(max_length=50)),
        ('title', models.CharField(max_length=50)),
        ('picture', models.ImageField(blank=True, null=True, upload_to=main.models.TeamMember.get_teammember_image_path)),
        ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
      ],
      options={
      },
      bases=(models.Model,),
    ),
  ]
