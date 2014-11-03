# -*- coding: utf-8 -*-

import factory
from product.models import Item, VariationType, Variation, ItemVariation


class VariationTypeFactory(factory.DjangoModelFatory):
    FACTORY_FOR = VariationType

    name = 'shoe size'


class VariationFactory(factory.DjangoModelFatory):
    FACTORY_FOR = Variation

    type = factory.SubFactory(VariationTypeFactory)
    name = '41'


class ItemFactory(factory.DjangoModelFatory):
    FACTORY_FOR = Item

    sku = 'SS1490'
    name = 'Coolest Dean'
    price = 9000
    gender = 'M'


class ItemVariationFactory(factory.DjangoModelFatory):
    FACTORY_FOR = ItemVariation

    item = factory.SubFactory(ItemFactory)
    Variation = factory.SubFactory(VariationFactory)



