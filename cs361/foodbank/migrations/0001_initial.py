# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=30)),
                ('category', models.CharField(default=b'O', max_length=5, choices=[(b'SP', b'Soup'), (b'GR', b'Grain'), (b'MT', b'Meat'), (b'FRUIT', b'Fruit'), (b'VEG', b'Vegetable'), (b'BEV', b'Beverage'), (b'P', b'Pasta'), (b'O', b'Other')])),
                ('unit', models.CharField(default=b'NA', max_length=5, choices=[(b'OZ', b'ounces'), (b'LB', b'pounds'), (b'G', b'grams'), (b'FL OZ', b'fluid ounces'), (b'L', b'liter'), (b'G', b'gallon'), (b'Q', b'quarts'), (b'NA', b'unknown')])),
                ('donation', models.ForeignKey(default=1, to='foodbank.Donation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(default=1, to='foodbank.Donor'),
            preserve_default=True,
        ),
    ]
