from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:cat_id>', categories, name='all_categories'),
    path('categories/', categories, name='all_categories'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:product_id>', show_product, name='product'),
]
