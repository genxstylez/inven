# -*- coding: utf-8 -*-

from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ['wiv__item__sku', 'wiv__item__name',]
