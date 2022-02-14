from unicodedata import category
from rest_framework import serializers
from offers.models import Offer, Category

class OfferSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(label='ID', read_only=True)
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    category_id = serializers.IntegerField(source='get_category_id')

    class Meta:
        model = Offer
        fields = ['id', 'title', 'price', 'category_id']


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField()
    ordering = serializers.IntegerField()
    class Meta:
        model = Offer
        fields = ['id', 'name', 'ordering']
