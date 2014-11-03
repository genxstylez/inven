# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def filterItem(formset, item_id):
    for form in formset:
        print dir(form.fields['iv'].valid_value())
        filtered_list = [i for i in formset.forms if i.item == item_id]
    return filtered_list
