# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_order_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_accepted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
