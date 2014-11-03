# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db import IntegrityError
from product.models import ItemVariation
from store.models import Store, StoreItemVariation


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
    siv = models.ForeignKey(StoreItemVariation, verbose_name=_('item'))
    description = models.CharField(_('description'), max_length=100, blank=True)
    created_at = models.DateField(_('created at'))
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

    def __unicode__(self):
        return '{} @ ${} ({})'.format(self.siv, self.price, self.get_type_display())


@receiver(post_save, sender=Order)
def update_store_stock(sender, instance, created, **kwargs):
    if created:
        instance.siv.quantity -= 1
        instance.siv.save()


@receiver(pre_delete, sender=Order)
def rollback_store_stock(sender, instance, **kwargs):
    instance.siv.quantity += 1
    instance.siv.save()


class Transfer(models.Model):
    from_store = models.ForeignKey(Store, verbose_name=_('From store'), related_name='from_stores')
    to_store = models.ForeignKey(Store, verbose_name=_('To store'), related_name='to_stores')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.from_store == self.to_store:
            raise IntegrityError('From and to cannot be the same')
        super(Transfer, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} ---> {}'.format(self.from_store, self.to_store)


class TransferItem(models.Model):
    transfer = models.ForeignKey(Transfer, related_name='items')
    iv = models.ForeignKey(ItemVariation, verbose_name=_('item'))
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return '{} ***{} ---> {}'.format(self.iv, self.quantity, self.transfer.to_store)


@receiver(post_save, sender=TransferItem)
def transfer_store(sender, instance, **kwargs):
    to_siv, created = StoreItemVariation.objects.get_or_create(store=instance.transfer.to_store, iv=instance.iv)
    to_siv.quantity += instance.quantity
    to_siv.save()

    from_siv = StoreItemVariation.objects.get(store=instance.transfer.from_store, iv=instance.iv)
    from_siv.quantity -= instance.quantity
    from_siv.save()


@receiver(pre_delete, sender=TransferItem)
def delete_transferitem(sender, instance, **kwargs):
    from_store = instance.transfer.from_store
    from_siv, created = StoreItemVariation.objects.get_or_create(store=from_store, iv=instance.iv)
    from_siv.quantity += instance.quantity
    from_siv.save()
    
    to_store = instance.transfer.to_store
    to_siv, created = StoreItemVariation.objects.get_or_create(store=to_store, iv=instance.iv)
    to_siv.quantity -= instance.quantity
    to_siv.save()
