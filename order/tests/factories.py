# -*- coding: utf-8 -*-

import factory
from order.models import Order, Transfer, TransferItem
from product.tests.factories import ItemVariationFactory
from store.test.factories import StoreFactory, StoreItemVariationFactory


class OrderFactory(factory.DjangoModelFatory):
    FACTORY_FOR = Order

    siv = factory.SubFactory(StoreItemVariationFactory)
    price = 9000
    type = '2'
    description = 'talk to the hand'


class TransferFactory(factory.DjangoModelFatory):
    FACTORY_FOR = Transfer

    from_store = factory.SubFactory(StoreFactory)
    to_store = factory.SubFactory(StoreFactory)


class TransferItemFactory(factory.DjangoModelFatory):
    FACTORY_FOR = TransferItem

    type = factory.SubFactory(TransferFactory)
    iv = factory.SubFactory(ItemVariationFactory)

    quantity = 5
    