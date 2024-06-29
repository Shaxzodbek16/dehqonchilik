from django.urls import path
from .views import product, store, news, contact, confirm


urlpatterns = [
    path('', news, name='news'),
    path('product/', product, name='product'),
    path('store/', store, name='store'),
    path('contact/', contact, name='contact'),
    path('confirm/', confirm, name='confirm'),
]
