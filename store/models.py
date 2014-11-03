# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from product.models import ItemVariation


class Store(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=200, blank=True)
    vat = models.PositiveIntegerField(_('vat'), blank=True)
    address = models.CharField(_('address'), max_length=300)

    def __unicode__(self):
        return self.name


class StoreItemVariation(models.Model):
    store = models.ForeignKey(Store, verbose_name=_('store'))
    iv = models.ForeignKey(ItemVariation, related_name='in_stores')
    quantity = models.PositiveSmallIntegerField(_('quantity'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

    def __unicode__(self):
        return '{} - {}'.format(self.store, self.iv)
