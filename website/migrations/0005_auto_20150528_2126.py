# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150528_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='user_id',
            new_name='user',
        ),
    ]
