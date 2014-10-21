# -*- coding: utf-8 -*-


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    name = models.CharField(_('name'), max_length=200)
    price = models.PositiveIntegerField(_('price'))

    def __unicode__(self):
        return self.name


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
