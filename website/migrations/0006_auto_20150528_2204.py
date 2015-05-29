# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150528_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='is_paid',
            field=models.BooleanField(default=0),
        ),
    ]
