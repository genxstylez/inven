# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from product.models import Item, Variation, ItemVariation


class Warehouse(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=200, blank=True)
    vat = models.PositiveIntegerField(_('vat'))
    address = models.CharField(_('address'), max_length=300)

    def __unicode__(self):
        return self.name


class WarehouseItemVariation(models.Model):
    warehouse = models.ForeignKey(Warehouse, verbose_name=_('warehouse'))
    item = models.ForeignKey(Item, verbose_name=('item'))
    variation = models.ForeignKey(Variation, verbose_name=('variation'))
    quantity = models.PositiveSmallIntegerField(_('quantity'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.warehouse, self.item, self.variation)


def update_stock(sender, instance, **kwargs):
    iv, created = ItemVariation.objects.get_or_create(item=instance.item, variation=instance.variation)
    wivs = WarehouseItemVariation.objects.filter(item=instance.item, variation=instance.variation)
    quantity = 0
    for wiv in wivs:
        quantity += wiv.quantity
    iv.quantity = quantity
    iv.save()

post_save.connect(update_stock, sender=WarehouseItemVariation)
