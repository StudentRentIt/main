# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_school_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='slug',
            field=models.SlugField(max_length=110, editable=False),
            preserve_default=True,
        ),
    ]
