# -*- coding: utf-8 -*-

from django.contrib import admin
from product.models import Item, VariationType, Variation, ItemVariation


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(VariationType)
class VariationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('type', 'name')


@admin.register(ItemVariation)
class ItemVariationAdmin(admin.ModelAdmin):
    list_display = ('item', 'variation', 'quantity')
    