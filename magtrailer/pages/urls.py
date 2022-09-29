from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('categories/<slug:cat_slug>', categories, name='all_categories'),
    path('categories/', categories, name='all_categories'),
    path('about/', about, name='about'),
    path('contacts/ok_form', ok_form, name='ok_form'),
    path('contacts/', contacts, name='contacts'),
    path('product/<slug:product_slug>', show_product, name='product'),
]
