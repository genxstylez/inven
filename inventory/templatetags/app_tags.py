# -*- coding: utf-8 -*-

from django import template
from product.models import ItemVariation
from store.models import StoreItemVariation


register = template.Library()


@register.simple_tag
def show_quantity(store, item, variation):
    iv = ItemVariation.objects.get(item=item, variation=variation)
    try:
        siv = StoreItemVariation.objects.get(store=store, iv=iv)
        return siv.quantity
    except StoreItemVariation.DoesNotExist:
        return 0

