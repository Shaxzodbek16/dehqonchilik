from django.urls import path
from .views import main_and_contact, confirm, contact


urlpatterns = [
    path('', main_and_contact, name='main'),
    path('confirm/', confirm, name='confirm'),
]
