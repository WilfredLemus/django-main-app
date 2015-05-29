# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150528_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMeal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('meal', models.ForeignKey(to='website.Order')),
                ('order', models.ForeignKey(to='website.Meal')),
            ],
        ),
    ]
