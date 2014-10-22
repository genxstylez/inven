# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from warehouse.forms import TransferForm


@staff_member_required
def transfer(request):
    template_name = 'warehouse/transfer.html'
    form = TransferForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, template_name, {'form': form})
