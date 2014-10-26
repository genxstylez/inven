# -*- coding: utf-8 -*-

from django.contrib import admin
from order.models import Order, Transfer


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ['wiv__item__sku', 'wiv__item__name',]


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ['from_wiv__item__sku, from_wiv__item__name', 'to_warehouse__name']
