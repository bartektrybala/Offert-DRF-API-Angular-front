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

        # DELETE - delete an offer
 
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
        # 404 - no offer of given id found

        url = reverse('offer', kwargs={'id': 3})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_invalid_post_offer1(self):

        # POST - add an offer
        # 400 - invalid field input

        url = reverse('offer', kwargs={'id': 6})
        data = {
            'title': 'some new offer',
            'price': 'abc', # <--- invalid field input
            'category_id': 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_post_offer2(self):

        # POST - add an offer
        # 400 - no category of given id found

        url = reverse('offer', kwargs={'id': 6})
        data = {
            'title': 'some new offer',
            'price': 1.20,
            'category_id': 2 # <--- no category of given id found
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_put_offer1(self):

        # PUT - modify an offer
        # 404 - no offer of given id found
 
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
        # 400 - invalid field input
 
        url = reverse('offer', kwargs={'id': 1})
        data = {
            'title': 'Apples',
            'price': 'abc', # <--- invalid field input
            'category_id': 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_delete_offer(self):

        # DELETE - delete an offer
        # 404 - no offer of given id found
 
        url = reverse('offer', kwargs={'id': 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)


class InvalidOfferTestCase2(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_invalid_get_offers(self):

        # GET - return all offers
        # 404 - no offers in DB

        url = reverse('offers')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

class ValidCategoryTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        category_apple = CategoryFactory(
            name = 'Apple',
            ordering = 1
        )
        category_pineapple = CategoryFactory(
            name = 'Pineapple',
            ordering = 3
        )
        category_strawberry = CategoryFactory(
            name = 'Strawberry',
            ordering = 2
        )

        self.category_list = (category_apple.ordering, category_strawberry.ordering, category_pineapple.ordering) # (1,2,3)

        
    def test_valid_get_categories(self):

        # GET - return all categories

        url = reverse('categories')

        response = self.client.get(url)

        for i in range(3):
            ordering = response.data[i]['ordering']
            self.assertEqual(self.category_list[i], ordering)

    def test_valid_get_category(self):

        # GET - return single category

        url = reverse('category', kwargs={'id': 2})
        
        response = self.client.get(url)

        category = Category.objects.get(id=2)
        serializer = CategorySerializer(category)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_valid_post_category(self):

        # POST - add single category

        url = reverse('category', kwargs={'id': 4})

        data = {
            'name': 'some new category',
            'ordering': 4
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)

    def test_valid_put_category(self):

        # PUT - modify single category

        url = reverse('category', kwargs={'id': 2})

        data = {
            'name': 'some changed category',
            'ordering': 4
        }
        
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, 202)

    def test_valid_delete_category(self):

        # DELETE - delete single category

        url = reverse('category', kwargs={'id': 2})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

class InvalidCategoryTestCase(APITestCase):

    def setUp(self):

        self.client = APIClient()
        
        CategoryFactory(
            name = 'Apple',
            ordering = 2
        )
        CategoryFactory(
            name = 'Banana',
            ordering = 4
        )

    def test_invalid_get_category(self):

        # GET - return single category
        # 404 - no category of given id

        url = reverse('category', kwargs={'id': 3})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_invalid_post_category1(self):

        # POST - add single category
        # 409 - same 'ordering' field value on another object

        url = reverse('category', kwargs={'id': 3})

        data = {
            'name': 'some_new_category',
            'ordering': 2 # <--- same 'ordering' field value on another object
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 409)

    def test_invalid_post_category2(self):

        # POST - add single category
        # 409 - same 'name' field value on another object

        url = reverse('category', kwargs={'id': 3})

        data = {
            'name': 'Apple', # <--- same 'name' field value on another object
            'ordering': 1
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 409)

    def test_invalid_put_category1(self):

        # PUT - modify single category
        # 409 - same 'ordering' field value on another object

        url = reverse('category', kwargs={'id': 2})

        data = {
            'name': 'Apple', 
            'ordering': 2 # <--- same 'ordering' field value on another object
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, 409)

    def test_invalid_put_category2(self):

        # PUT - modify single category
        # 409 - same 'name' field value on another object

        url = reverse('category', kwargs={'id': 2})

        data = {
            'name': 'Apple', # <--- same 'name' field value on another object
            'ordering': 1
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, 409)
    
    def test_invalid_delete_category(self):

        # DELETE - delete single category
        # 404 - no category of given id found

        url = reverse('category', kwargs={'id': 5})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)


class InvalidCategoryTestCase2(APITestCase):

    def setUp(self):

        self.client = APIClient()

    def test_invalid_get_categories(self):

        # GET - return all categories
        # 404 - no categories in DB

        url = reverse('categories')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


        



        


        





