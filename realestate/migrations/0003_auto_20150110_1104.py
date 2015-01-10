# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import realestate.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=realestate.models.Company.get_company_logo_path, null=True, blank=True),
            preserve_default=True,
        ),
    ]
