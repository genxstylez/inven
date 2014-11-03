# -*- codoing: utf-8 -*-
from __future__ import unicode_literals


from django.test import TestCase
from store.models import Store
from store.tests.factories import StoreFactory, StoreItemVariationFactory, create_stores


class StoreTest(TestCase):
    @classmethod
    def setUpClass(cls):
        Store.objects.all().delete()
        create_stores()

    @classmethod
    def tearDownClass(cls):
        Store.objects.all().delete()

