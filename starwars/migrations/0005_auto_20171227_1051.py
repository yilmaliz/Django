# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0004_auto_20171227_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='Race',
            field=models.CharField(max_length=100, default='Human', choices=[('0', 'Whill'), ('1', 'Human'), ('2', 'Kaleesh'), ('3', 'Cyborg'), ('4', 'Zabrak'), ('5', 'Korun'), ('6', 'Droid'), ('7', 'Clone'), ('8', 'Kel Dor'), ('9', 'Wookiee'), ('10', 'Hutt')]),
        ),
        migrations.AddField(
            model_name='character',
            name='Side',
            field=models.CharField(max_length=100, default='Dark Side', choices=[('0', 'Dark Side'), ('1', 'Light Side')]),
        ),
    ]
