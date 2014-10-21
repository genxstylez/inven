# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('type', models.CharField(default=b'2', max_length=2, verbose_name='item', choices=[(b'1', 'PR'), (b'2', 'Sales')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('wiv', models.ForeignKey(verbose_name='item', to='warehouse.WarehouseItemVariation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
