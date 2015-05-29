# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150528_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
