from rest_framework.views import APIView
from rest_framework.response import Response
from offers.models import Offer
from offers.serializers import OfferSerializer


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
        return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})