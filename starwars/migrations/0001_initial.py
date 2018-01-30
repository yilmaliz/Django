# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=100, blank=True, null=True)),
                ('Job', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=100, blank=True, null=True)),
                ('Year', models.DateField()),
                ('GamePage', models.URLField(blank=True, null=True)),
                ('VideoLink', models.URLField(blank=True, null=True)),
                ('Publisher', models.CharField(max_length=100, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=100, blank=True, null=True)),
                ('DirectorName', models.CharField(max_length=100, blank=True, null=True)),
                ('TrailerLink', models.URLField(blank=True, null=True)),
                ('Year', models.DateField()),
                ('ImdbPoint', models.CharField(max_length=10, blank=True, null=True)),
                ('isCartoon', models.BooleanField()),
                ('Charecters', models.ManyToManyField(to='starwars.Character')),
            ],
        ),
    ]
