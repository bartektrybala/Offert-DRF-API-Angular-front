from django.urls import path
from .views import *

offers_view = OfferViewSet.as_view({
    'get': 'get_offers'
})

categories_view = CategoryViewSet.as_view({
    'get': 'get_categories'
})

offer_by_id_view = OfferViewSet.as_view({
    'get': 'get_offer',
    'post': 'add_offer',
    'put': 'change_offer',
    'delete': 'delete_offer'
})

category_by_id_view = CategoryViewSet.as_view({
    'get': 'get_category',
    'post': 'add_category',
    'put': 'change_category',
    'delete': 'delete_category'
})

urlpatterns = [
    path('', api_overview, name='api-overwiew'),
    path('offers/', offers_view, name='offers'),
    path('offers/<int:id>', offer_by_id_view, name='offer'),
    path('category', categories_view, name='categories'),
    path('category/<int:id>', category_by_id_view, name='category')
] 






