# -*- coding: utf-8 -*-

from django.contrib import admin
from store.models import Store, StoreItemVariation


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'vat')


@admin.register(StoreItemVariation)
class StoreItemVariationAdmin(admin.ModelAdmin):
    list_display = ('store', 'iv', 'quantity')
    list_filter = ('store',)
    search_fields = ['iv__item__sku', 'iv__item__name']
