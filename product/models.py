# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class VariationType(models.Model):
    name = models.CharField(_('name'), max_length=100)  # e.g. Size

    def __unicode__(self):
        return self.name


class Variation(models.Model):
    type = models.ForeignKey(VariationType, related_name='variations', verbose_name=_('type'))
    name = models.CharField(_('name'), max_length=50)  # e.g. 41

    def __unicode__(self):
        return self.name


class Item(models.Model):
    GENDER_CHOICES = (
        ('M', _('male')),
        ('F', _('female'))
    )
    variation_type = models.ForeignKey(VariationType)
    sku = models.CharField(_('sku'), max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=200)
    price = models.PositiveIntegerField(_('price'))
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, default='M')

    def __unicode__(self):
        return '{} - {} ({})'.format(self.sku, self.name, self.gender)


class ItemVariation(models.Model):
    item = models.ForeignKey(Item, verbose_name='item', related_name='variations')
    variation = models.ForeignKey(Variation, verbose_name='variation')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)

    def __unicode__(self):
        return '{} #{}'.format(self.item, self.variation)

    @property
    def quantity(self):
        qty = 0
        for in_store in self.in_stores.all():
            qty += in_store.quantity
        return qty


@receiver(post_save, sender=Item)
def create_item_variation(sender, instance, created, **kwargs):
    variations = instance.variation_type.variations.all()
    for variation in variations:
        ItemVariation.objects.get_or_create(item=instance, variation=variation)
