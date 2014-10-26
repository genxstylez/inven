# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.db import IntegrityError
from warehouse.models import WarehouseItemVariation, Warehouse


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
    description = models.CharField(_('description'), max_length=100, blank=True)
    created_at = models.DateField(_('created at'))
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

    def __unicode__(self):
        return '{} @ ${} ({})'.format(self.wiv, self.price, self.get_type_display())


def update_warehouse_stock(sender, instance, created, **kwargs):
    if created:
        instance.wiv.quantity -= 1
        instance.wiv.save()


class Transfer(models.Model):
    from_wiv = models.ForeignKey(WarehouseItemVariation, verbose_name=_('item'))
    to_warehouse = models.ForeignKey(Warehouse, verbose_name=_('To warehouse'))
    quantity = models.PositiveSmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.from_wiv.warehouse == self.to_warehouse:
            raise IntegrityError('From and to cannot be the same')
        super(Transfer, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} *** {} -> {}'.format(self.from_wiv, self.quantity, self.to_warehouse)


def transfer_warehouse(sender, instance, **kwargs):
    try:
        wiv = WarehouseItemVariation.objects.get(warehouse=instance.to_warehouse, item=instance.from_wiv.item, variation=instance.from_wiv.variation)
        wiv.quantity += instance.quantity
        wiv.save()

        instance.from_wiv.quantity -= instance.quantity
        instance.from_wiv.save()

    except WarehouseItemVariation.DoesNotExist:
        WarehouseItemVariation.objects.create(
            warehouse=instance.to_warehouse,
            item=instance.from_wiv.item,
            variation=instance.from_wiv.variation,
            quantity=instance.quantity)

        instance.from_wiv.quantity -= instance.quantity
        instance.from_wiv.save()

def delete_transfer(sender, instance, **kwargs):
    from_wiv = instance.from_wiv
    from_wiv.quantity += instance.quantity
    from_wiv.save()


post_save.connect(update_warehouse_stock, sender=Order)
post_save.connect(transfer_warehouse, sender=Transfer)
pre_delete.connect(delete_transfer, sender=Transfer)
