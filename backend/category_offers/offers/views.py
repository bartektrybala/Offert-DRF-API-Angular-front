from rest_framework.response import Response
from offers.models import Offer, Category
from offers.serializers import CategorySerializer, OfferSerializer 
from rest_framework import status, viewsets

from rich import print

ERROR_NO_ITEM = 'NO SUCH ITEM'

class OfferViewSet(viewsets.ModelViewSet):

    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

    def get_offers(self, request):
        """
        Return a list of all offers, or a list of offers of a category (category's id) passed as a query parameter.
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
        Return an offer by its id.
        """
        offer_id = kwargs['id']
        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

    def add_offer(self, request, **kwargs):
        offer = OfferSerializer(data=request.data)
        if offer.is_valid():
            offer.save()
            return Response(offer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def change_offer(self, request, **kwargs):
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
        Return a list of all categories.
        """
        categories = Category.objects.order_by('ordering')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def get_category(self, request, **kwargs):
        category_id = kwargs['id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(ERROR_NO_ITEM)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def add_category(self, request, **kwargs):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def change_category(self, request, **kwargs):
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
        category_id = kwargs['id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(ERROR_NO_ITEM) 
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

