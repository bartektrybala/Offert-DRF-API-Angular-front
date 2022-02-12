from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< Updated upstream
from offers.models import Offer
from offers.serializers import OfferSerializer


=======
from rest_framework import authentication, permissions
from offers.models import Offer, Category
from offers.serializers import CategorySerializer, OfferSerializer 
>>>>>>> Stashed changes
class OfferList(APIView):
    """
    View to list all offers in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all offers.
        """
        offers = [offer for offer in Offer.objects.all()]
        serializer = OfferSerializer(offers, many=True)
<<<<<<< Updated upstream
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})
=======
        return Response(serializer.data)

class CategoryList(APIView):
    """
    View to list all categories in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all categories.
        """
        categories = Category.objects.all()
        
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

>>>>>>> Stashed changes
