# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

  dependencies = [
    ('realestate', '__first__'),
    ('main', '0002_user_phone_number'),
  ]

  operations = [
    migrations.AddField(
      model_name='user',
      name='real_estate_company',
      field=models.ForeignKey(blank=True, to='realestate.Company', null=True),
      preserve_default=True,
    ),
  ]
