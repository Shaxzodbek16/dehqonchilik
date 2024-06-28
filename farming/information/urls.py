from django.urls import path
from .views import product, store, news, contact


urlpatterns = [
    path('', news, name='news'),
    path('product/', product, name='product'),
    path('store/', store, name='store'),
    path('contact/', contact, name='contact'),
]
