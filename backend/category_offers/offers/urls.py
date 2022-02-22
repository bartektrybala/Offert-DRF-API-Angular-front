from django.urls import path
from .views import *

offers = OfferViewSet.as_view({
    'get': 'get_offers'
})

categories = CategoryViewSet.as_view({
    'get': 'get_categories'
})

offer_by_id = OfferViewSet.as_view({
    'get': 'get_offer',
    'post': 'add_offer',
    'put': 'change_offer',
    'delete': 'delete_offer'
})

category_by_id = CategoryViewSet.as_view({
    'get': 'get_category',
    'post': 'add_category',
    'put': 'change_category',
    'delete': 'delete_category'
})

urlpatterns = [
    path('', api_overview, name='api-overwiew'),
    path('offers/', offers, name='offers'),
    path('offers/<int:id>', offer_by_id, name='offer'),
    path('category', categories, name='categories'),
    path('category/<int:id>', category_by_id, name='category')
] 






