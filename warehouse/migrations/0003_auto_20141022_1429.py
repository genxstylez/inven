# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20141021_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseitemvariation',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='quantity'),
        ),
    ]
