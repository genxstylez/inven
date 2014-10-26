# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    GENDER_CHOICES = (
        ('M', _('male')),
        ('F', _('female'))
    )
    sku = models.CharField(_('sku'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=200)
    price = models.PositiveIntegerField(_('price'))
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, default='M')

    def __unicode__(self):
        return '{} - {} ({})'.format(self.sku, self.name, self.gender)


class VariationType(models.Model):
    name = models.CharField(_('name'), max_length=100)  # e.g. Size

    def __unicode__(self):
        return self.name


class Variation(models.Model):
    type = models.ForeignKey(VariationType, related_name='variations', verbose_name=_('type'))
    name = models.CharField(_('name'), max_length=50)  # e.g. 41

    def __unicode__(self):
        return self.name


class ItemVariation(models.Model):
    item = models.ForeignKey(Item, verbose_name='item')
    variation = models.ForeignKey(Variation, verbose_name='variation')
    quantity = models.PositiveSmallIntegerField(_('quantity'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)
