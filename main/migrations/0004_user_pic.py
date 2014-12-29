# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user_real_estate_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(null=True, upload_to=main.models.User.get_user_image_path, blank=True),
            preserve_default=True,
        ),
    ]
