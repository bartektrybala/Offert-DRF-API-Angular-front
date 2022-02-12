from rest_framework import serializers
from offers.models import Offer, Category

class OfferSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(label='ID', read_only=True)
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'price']


    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # title = models.TextField(max_length=200)
    # description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField()
    ordering = serializers.IntegerField()
    class Meta:
        model = Offer
        fields = ['id', 'name', 'ordering']

    # class Category(models.Model):
    # name = models.TextField()
    # ordering = models.IntegerField(unique=True)