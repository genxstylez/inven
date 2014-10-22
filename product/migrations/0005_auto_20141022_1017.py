# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_item_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, verbose_name='gender', choices=[(b'M', 'male'), (b'F', 'female')]),
        ),
    ]
