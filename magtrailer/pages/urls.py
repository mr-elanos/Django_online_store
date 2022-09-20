from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('categories/', categories, name='all_categories'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
