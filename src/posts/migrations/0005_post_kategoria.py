# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160125_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kategoria',
            field=models.CharField(choices=[('MI', 'Miesa'), ('NA', 'Napoje'), ('GA', 'Garmazeria'), ('AS', 'Artykuly spozywcze')], default='AS', max_length=2),
        ),
    ]
