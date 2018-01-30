# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0009_auto_20171229_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Race',
            field=models.CharField(max_length=100, default='Human', choices=[('Whill', 'Whill'), ('Human', 'Human'), ('Kaleesh', 'Kaleesh'), ('Cyborg', 'Cyborg'), ('Zabrak', 'Zabrak'), ('Korun', 'Korun'), ('Droid', 'Droid'), ('Clone', 'Clone'), ('Kel Dor', 'Kel Dor'), ('Wookiee', 'Wookiee'), ('Hutt', 'Hutt')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='Text',
            field=models.TextField(max_length=5000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Type',
            field=models.CharField(max_length=100, default='Human', choices=[('0', 'Movie'), ('1', 'Cartoon')]),
        ),
    ]
