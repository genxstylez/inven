# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('vat', models.PositiveIntegerField(verbose_name='vat')),
                ('address', models.CharField(max_length=300, verbose_name='address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WarehouseItemVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('item', models.ForeignKey(verbose_name=b'item', to='product.Item')),
                ('variation', models.ForeignKey(verbose_name=b'variation', to='product.Variation')),
                ('warehouse', models.ForeignKey(verbose_name='warehouse', to='warehouse.Warehouse')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
