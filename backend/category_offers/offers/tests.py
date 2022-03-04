import datetime
import json

import factory
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rich import print

from .serializers import OfferSerializer, CategorySerializer
from .models import Category, Offer


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer
        
class ValidOfferTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        category_apple = CategoryFactory(
            name = 'Apple',
            ordering = 1
            )

        for i in range(5):
            OfferFactory(
                title = 'Apples',
                category = category_apple,
                description = f'{i} apples',
                price = i*0.50
                )
        
    def test_valid_get_offers(self):

        # GET - return all offers

        url = reverse('offers')

        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)

        response = self.client.get(url)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)


    def test_valid_get_offer(self):

        # GET - return single offer

        url = reverse('offer', kwargs={'id': 3})

        offer = Offer.objects.get(id=3)
        serializer = OfferSerializer(offer)

        response = self.client.get(url)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_valid_post_offer(self):

        # POST - add an offer

        url = reverse('offer', kwargs={'id': 6})
        data = {
            'title': 'some new offer',
            'price': 1.60,
            'category_id': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_valid_put_offer(self):

        # PUT - modify an offer
 
        url = reverse('offer', kwargs={'id': 2})
        data = {
            'title': 'Apples',
            'price': 10.30,
            'category_id': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 202)

    def test_valid_delete_offer(self):

        # DELETE - modify an offer
 
        url = reverse('offer', kwargs={'id': 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

        
class InvalidOfferTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        category_apple = CategoryFactory(
            name = 'Apple',
            ordering = 1
        )

        offer = OfferFactory(
            category = category_apple,
            title = 'Apples',
            description = 'blabla',
            price = 12.30,
        )

    def test_invalid_get_offer(self):

        # GET - return single offer

        url = reverse('offer', kwargs={'id': 3})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_invalid_post_offer1(self):

        # POST - add an offer

        url = reverse('offer', kwargs={'id': 6})
        data = {
            'title': 'some new offer',
            'price': 'abc',             # <--- invalid field input
            'category_id': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_post_offer2(self):

        # POST - add an offer

        url = reverse('offer', kwargs={'id': 6})
        data = {
            'title': 'some new offer',
            'price': 1.20,
            'category_id': 2            # <--- no such category
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_put_offer1(self):

        # PUT - modify an offer
 
        url = reverse('offer', kwargs={'id': 2})
        data = {
            'title': 'Apples',
            'price': 10.30,
            'category_id': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 404)

    def test_invalid_put_offer2(self):

        # PUT - modify an offer
 
        url = reverse('offer', kwargs={'id': 1})
        data = {
            'title': 'Apples',
            'price': 'abc',
            'category_id': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_delete_offer(self):

        # DELETE - modify an offer
 
        url = reverse('offer', kwargs={'id': 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)


class InvalidOfferTestCase2(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_invalid_get_offers(self):

        # GET - return all offers

        url = reverse('offers')

        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


        





