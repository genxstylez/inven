# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('type', models.CharField(default='2', max_length=2, verbose_name='type', choices=[('1', 'PR'), ('2', 'Sales')])),
                ('description', models.CharField(max_length=100, verbose_name='description', blank=True)),
                ('created_at', models.DateField(verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('siv', models.ForeignKey(verbose_name='item', to='store.StoreItemVariation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('from_store', models.ForeignKey(related_name='from_stores', verbose_name='From store', to='store.Store')),
                ('to_store', models.ForeignKey(related_name='to_stores', verbose_name='To store', to='store.Store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransferItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('iv', models.ForeignKey(verbose_name='item', to='product.ItemVariation')),
                ('transfer', models.ForeignKey(related_name='items', to='order.Transfer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
