# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0005_auto_20171227_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
