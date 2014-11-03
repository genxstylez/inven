# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import formset_factory
from product.models import Item
from order.models import Transfer, TransferItem


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer


class TransferItemForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), required=False)

    class Meta:
        model = TransferItem
        exclude = ('transfer', )

    def __init__(self, *args, **kwargs):
        super(TransferItemForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'form-control qty'

TransferItemFormSet = formset_factory(TransferItemForm, extra=0)
