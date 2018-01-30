# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0006_auto_20171227_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
