# -*- coding: utf-8 -*-

from django import forms
from warehouse.models import Warehouse, WarehouseItemVariation


class TransferForm(forms.Form):
    from_wiv = forms.ModelChoiceField(queryset=WarehouseItemVariation.objects.all())
    to = forms.ModelChoiceField(queryset=Warehouse.objects.all())
    quantity = forms.IntegerField()

    def save(self):
        cleaned_data = super(TransferForm, self).clean()
        from_wiv = cleaned_data['from_wiv']
        to = cleaned_data['to']
        wiv, created = WarehouseItemVariation.objects.get_or_create(warehouse=to, item=from_wiv.item, variation=from_wiv.variation)
        wiv.quantity += cleaned_data['quantity']
        from_wiv.quantity -= cleaned_data['quantity']
        wiv.save()
        from_wiv.save()

