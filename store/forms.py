# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import formset_factory

from store.models import StoreItemVariation
from product.models import Item


class StoreItemVariationForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), required=False)

    class Meta:
        model = StoreItemVariation
        exclude = ('store', )

    def __init__(self, *args, **kwargs):
        super(StoreItemVariationForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'form-control qty'


StoreItemVariationFormSet = formset_factory(StoreItemVariationForm, extra=0)
