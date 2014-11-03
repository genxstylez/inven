# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse, HttpResponseBadRequest
from product.models import Item, VariationType
from store.forms import StoreItemVariationFormSet
from store.models import Store, StoreItemVariation


@staff_member_required
def check_stock(request, store_id, iv_id):
    siv = StoreItemVariation.objects.get(store__id=store_id, iv__id=iv_id)
    quantity = int(request.GET.get('quantity', 0))
    if quantity > 0:
        if siv.quantity - quantity >= 0:
            return HttpResponse(True)
        
    return HttpResponseBadRequest()


@staff_member_required
def add_stock(request, type='Shoe Size'):
    stores = Store.objects.all()
    variation_type = VariationType.objects.get(name=type)
    items = Item.objects.filter(variation_type=variation_type)

    ivs = []
    for item in items:
        ivs += list(item.variations.all())

    data = [{'iv': iv.id, 'item': iv.item.id} for iv in ivs]
    formset = StoreItemVariationFormSet(request.POST or None, initial=data)

    if formset.is_valid() and 'store' in request.POST:
        for form in formset:
            if form.cleaned_data['quantity'] > 0:
                instance = form.save(commit=False)
                instance.store = Store.objects.get(id=request.POST['store'])
                siv, created = StoreItemVariation.objects.get_or_create(store=instance.store, iv=instance.iv)
                siv.quantity += instance.quantity
                siv.save()
                
        return redirect('add-stock')

    return render(request, 'store/add.html', {
        'stores': stores,
        'formset': formset,
        'items': items,
        'variations': variation_type.variations.all()
    })
