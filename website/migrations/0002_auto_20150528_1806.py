# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_paid', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.AddField(
            model_name='sell',
            name='order_id',
            field=models.ForeignKey(to='website.Order'),
        ),
        migrations.AddField(
            model_name='sell',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
