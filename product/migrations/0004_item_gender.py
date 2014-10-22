# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_item_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gender',
            field=models.CharField(default='M', max_length=1, verbose_name='gender', choices=[(b'M', 'male'), (b'F', 'female')]),
            preserve_default=False,
        ),
    ]
