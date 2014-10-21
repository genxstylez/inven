# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(default=b'2', max_length=2, verbose_name='type', choices=[(b'1', 'PR'), (b'2', 'Sales')]),
        ),
    ]
