from rest_framework.response import Response
from offers.models import Offer, Category
from offers.serializers import CategorySerializer, OfferSerializer 
from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from rich import print

ERROR_NO_ITEM = 'NO SUCH ITEM'


@api_view(('GET',))
def api_overview(request):
    api_urls = {
        '/offers': 'returns all offers(query parameter = ?category=category_id',
        '/category': 'returns all categories sorted by ordering field',
        '/offers/id': 'GET, POST, PUT and DELETE methods for a single offer',
        '/category/id': 'GET, POST, PUT and DELETE methods for a single category',
    }
    return Response(api_urls)

class OfferViewSet(viewsets.ModelViewSet):

    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

    def get_offers(self, request):
        """
        GET all offers | query parameter 'category'
        """
        category_id = request.query_params.get('category', None)

        if category_id is None:
            offers = Offer.objects.all()
        else:
            offers = Offer.objects.filter(category__id=category_id)
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)

    def get_offer(self, request, **kwargs):
        """
        GET single offer
        """
        offer_id = kwargs['id']
        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

    def add_offer(self, request, **kwargs):
        """
        POST single offer
        """
        offer = OfferSerializer(data=request.data)
        if offer.is_valid():
            offer.save()
            return Response(offer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def change_offer(self, request, **kwargs):
        """
        PUT single offer
        """
        offer_id = kwargs['id']
        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        serializer = OfferSerializer(instance=offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete_offer(self, request, **kwargs):
        """
        DELETE single offer
        """
        offer_id = kwargs['id']
        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_categories(self, request):
        """
        GET all categories
        """
        categories = Category.objects.order_by('ordering')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def get_category(self, request, **kwargs):
        """
        GET single category
        """
        category_id = kwargs['id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def add_category(self, request, **kwargs):
        """
        POST single category
        """
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def change_category(self, request, **kwargs):
        """
        PUT single category
        """
        category_id = kwargs['id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete_category(self, request, **kwargs):
        """
        DELETE single category
        """
        category_id = kwargs['id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(ERROR_NO_ITEM) 
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

