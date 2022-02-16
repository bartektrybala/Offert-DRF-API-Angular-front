from tokenize import Single
from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiOverview, name='home'),
    path('offers', OfferList.as_view(), name='offers'),
    path('category', CategoryList.as_view(), name='category'),
    path('offers/<int:id>', SingleOfferList.as_view(), name='offer')
]




