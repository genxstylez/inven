# -*- coding: utf-8 -*-

from django.contrib import admin
from warehouse.models import Warehouse, WarehouseItemVariation


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'vat')


@admin.register(WarehouseItemVariation)
class WarehouseItemVariation(admin.ModelAdmin):
    list_display = ('warehouse', 'item', 'variation', 'quantity')
