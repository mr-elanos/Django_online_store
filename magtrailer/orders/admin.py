from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'date', 'is_finished')
    list_filter = ('date', 'is_finished',)
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
