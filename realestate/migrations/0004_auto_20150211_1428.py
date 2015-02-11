# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
from django.conf import settings
import realestate.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0003_auto_20150110_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='contact',
            field=models.ForeignKey(null=True, blank=True, help_text='By choosing a contact, that contact will show on all your properties. By leaving this        blank, each time a property is loaded a random agent from your company will be shown. If you want         certain agents to be shown for certain properties, you need to set that on the Edit Property.', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='default_school',
            field=models.ForeignKey(null=True, blank=True, help_text='This school will be shown when users search by your company properties.', to='school.School'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(help_text='This image will show on properties that the agent has not chosen a default picture         through Edit Profile. If there is no agent picture nor a default company logo, a RentVersity         logo will be shown.', upload_to=realestate.models.Company.get_company_logo_path, null=True, blank=True),
            preserve_default=True,
        ),
    ]
