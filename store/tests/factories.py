# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from store.models import Store, StoreItemVariation
from product.tests.factories import ItemVariationFactory


class StoreFactory(factory.DjangoModelFatory):
    FACTORY_FOR = Store

    name = 'Selfridges'


class StoreItemVariationFactory(factory.DjangoModelFatory):
    FACTORY_FOR = StoreItemVariation

    store = factory.SubFactory(StoreFactory)
    iv = factory.SubFactory(ItemVariationFactory)
    quantity = 10


def create_stores():
    StoreFactory.create(name='Selfridges')
    StoreFactory.create(name='EMPOR')
    StoreFactory.create(name='House of Fraser')
    