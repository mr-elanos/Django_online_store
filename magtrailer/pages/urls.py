from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('categories/<slug:cat_slug>', ShowCategories.as_view(), name='show_categories'),
    path('categories/', AllCategories.as_view(), name='all_categories'),
    path('about/', about, name='about'),
    path('contacts/ok_form/', ok_form, name='ok_form'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('buy_and_delivery/', buy_and_delivery, name='buy_and_delivery'),
    path('search_result/', Search.as_view(), name='search_result')
]
