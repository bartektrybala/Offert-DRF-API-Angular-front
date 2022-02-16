from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from offers.models import Offer, Category
from offers.serializers import CategorySerializer, OfferSerializer 

from rich import print

@api_view(['GET'])
def ApiOverview(request):

    api_urls = {
        'all_offers': '/offers',
        'offers_by_category': '/offers?category=category_id',
        'all_categories': '/category',
        'offer_by_id': '/offers/ID',
    }
  
    return Response(api_urls)

class OfferList(APIView):

    def get(self, request, format=None):
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


class SingleOfferList(APIView):
    
    def get(self, request, format=None, **kwargs):
        """
        Return an offer by its id.
        """
        offer_id = self.kwargs['id']
        offer = Offer.objects.get(id=offer_id)
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

class CategoryList(APIView):

    def get(self, request, format=None):
        """
        Return a list of all categories.
        """
        categories = Category.objects.order_by('ordering')
        
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

