# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20141022_1429'),
        ('order', '0004_auto_20141022_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('from_wiv', models.ForeignKey(verbose_name='item', to='warehouse.WarehouseItemVariation')),
                ('to_warehouse', models.ForeignKey(verbose_name='To warehouse', to='warehouse.Warehouse')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
