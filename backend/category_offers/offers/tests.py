import datetime
import json

import factory
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from rich import print

from .models import Category, Offer


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'Apple'
    ordering = 1

class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    title = 'Apples'
    description = '3 apples'
    price = 1.50
    created_at = datetime.datetime.now()
        
class OfferTestCase(APITestCase):


    def setUp(self):
        self.r_factory = APIRequestFactory()
        self.client = APIClient()

        category_apple = CategoryFactory()
        for i in range(5):
            OfferFactory(category=category_apple, description=f'{i} apples', price=i*0.50)
        
    def test_get_offers(self):

        # GET - return all offers

        url = reverse('offers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_offer(self):

        # GET - return single offer

        url = reverse('offer', kwargs={'id': 3})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_offer(self):

        # POST - add an offer

        url = reverse('offer', kwargs={'id': 6})
        data = {
            'title': 'some new offer',
            'price': 1.60,
            'category_id': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_put_offer(self):

        # PUT - modify an offer
 
        url = reverse('offer', kwargs={'id': 2})
        data = {
            'title': 'Apples',
            'price': 10.30,
            'category_id': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 202)

    def test_delete_offer(self):

        # DELETE - modify an offer
 
        url = reverse('offer', kwargs={'id': 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        
        






        





