from unicodedata import category
from rest_framework import serializers
from offers.models import Offer, Category
from rest_framework.response import Response

from rich import print

class OfferSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(label='ID', read_only=True)
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    category_id = serializers.IntegerField(source='category.id')

    class Meta:
        model = Offer
        fields = ['id', 'title', 'price', 'category_id']

    def create(self, validated_data):
        category_id = validated_data['category']['id']
        
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            error = 'There is no category with given id'
            return Response(error)
        validated_data['category'] = category
 
        return Offer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        category_id = validated_data['category']['id']

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            error = 'There is no category with given id'
            return Response(error)

        instance.title = validated_data['title']
        instance.price = validated_data['price']
        instance.category = category
        instance.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField()
    ordering = serializers.IntegerField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'ordering']
