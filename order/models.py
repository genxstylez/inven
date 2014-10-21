# -*- coding: utf-8 -*-


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from warehouse.models import WarehouseItemVariation


class Order(models.Model):
    '''
    One order per Sales
    '''
    TYPE_CHOICES = (
        ('1', _('PR')),
        ('2', _('Sales'))
    )

    price = models.PositiveIntegerField(_('price'))
    type = models.CharField(_('type'), max_length=2, choices=TYPE_CHOICES, default='2')
    wiv = models.ForeignKey(WarehouseItemVariation, verbose_name=_('item'))
    created_at = models.DateTimeField(_('created at'))
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)


def update_warehouse_stock(sender, instance, **kwargs):
    instance.wiv.quantity -= 1
    instance.wiv.save()


post_save.connect(update_warehouse_stock, sender=Order)
