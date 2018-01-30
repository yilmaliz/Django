# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='game',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
