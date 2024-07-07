from django.urls import path
from .views import main_page, confirm


urlpatterns = [
    path('', main_page, name='main'),
    path('confirm/', confirm, name='confirm'),
]
