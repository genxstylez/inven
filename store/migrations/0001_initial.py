# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=200, verbose_name='description', blank=True)),
                ('vat', models.PositiveIntegerField(verbose_name='vat', blank=True)),
                ('address', models.CharField(max_length=300, verbose_name='address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreItemVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('iv', models.ForeignKey(related_name='in_stores', to='product.ItemVariation')),
                ('store', models.ForeignKey(verbose_name='store', to='store.Store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
