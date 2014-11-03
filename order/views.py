# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from product.models import Item, VariationType
from order.models import Transfer
from order.forms import TransferItemFormSet
from store.models import Store


@staff_member_required
def transfer_stock(request, type='Shoe Size'):
    stores = Store.objects.all()
    variation_type = VariationType.objects.get(name=type)
    items = Item.objects.filter(variation_type=variation_type)

    ivs = []
    for item in items:
        ivs += list(item.variations.all())

    data = [{'iv': iv.id, 'item': iv.item.id} for iv in ivs]
    formset = TransferItemFormSet(request.POST or None, initial=data)

    if formset.is_valid() and 'from_store' in request.POST and 'to_store' in request.POST:
        from_store = Store.objects.get(id=request.POST['from_store'])
        to_store = Store.objects.get(id=request.POST['to_store'])
        transfer = Transfer.objects.create(to_store=to_store, from_store=from_store)
        for form in formset:
            if form.cleaned_data['quantity'] > 0:
                instance = form.save(commit=False)
                instance.transfer = transfer
                instance.save()
        return redirect('transfer-stock')

    return render(request, 'order/transfer.html', {
        'stores': stores,
        'formset': formset,
        'items': items,
        'variations': variation_type.variations.all()
    })
