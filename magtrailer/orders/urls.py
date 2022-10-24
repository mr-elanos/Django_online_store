from django.urls import re_path
from .views import order_create

app_name = 'orders'

urlpatterns = [
    re_path(r'^create/$', order_create, name='order_create'),
]
