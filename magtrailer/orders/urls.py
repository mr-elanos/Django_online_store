from django.urls import re_path, path
from .views import order_create, ok_order

app_name = 'orders'

urlpatterns = [
    path('ok_order', ok_order, name='ok_order'),
    re_path(r'^create/$', order_create, name='order_create'),

]
