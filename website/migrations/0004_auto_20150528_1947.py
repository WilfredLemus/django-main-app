# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_ordermeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermeal',
            name='meal',
            field=models.ForeignKey(to='website.Meal'),
        ),
        migrations.AlterField(
            model_name='ordermeal',
            name='order',
            field=models.ForeignKey(to='website.Order'),
        ),
    ]
