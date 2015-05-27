# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seat_number',
            field=models.PositiveSmallIntegerField(default=-1),
            preserve_default=False,
        ),
    ]
