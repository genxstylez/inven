# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(unique=True, max_length=100, verbose_name='sku')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('gender', models.CharField(default='M', max_length=1, verbose_name='gender', choices=[('M', 'male'), ('F', 'female')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('item', models.ForeignKey(verbose_name='item', to='product.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='variation',
            name='type',
            field=models.ForeignKey(related_name='variations', verbose_name='type', to='product.VariationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemvariation',
            name='variation',
            field=models.ForeignKey(verbose_name='variation', to='product.Variation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='variation_type',
            field=models.ForeignKey(to='product.Variation'),
            preserve_default=True,
        ),
    ]
