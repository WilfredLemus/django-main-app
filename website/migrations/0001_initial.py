# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('table_id', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('seat_number', models.PositiveSmallIntegerField()),
                ('price', models.FloatField(default=0)),
                ('table', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_served', models.BooleanField()),
                ('is_accepted', models.BooleanField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderMeal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('meal', models.ForeignKey(to='website.Meal')),
                ('order', models.ForeignKey(to='website.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('meal_id', models.ForeignKey(to='website.Meal')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=0)),
                ('order', models.ForeignKey(to='website.Order')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMeal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='type_id',
            field=models.ForeignKey(to='website.TypeMeal'),
        ),
    ]
