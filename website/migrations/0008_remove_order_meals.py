# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='meals',
        ),
    ]
