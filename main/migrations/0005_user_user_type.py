# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('STU', 'Student'), ('BOW', 'Business Owner'), ('MGR', 'Landlord/Manager')], max_length=30, blank=True, null=True),
            preserve_default=True,
        ),
    ]
