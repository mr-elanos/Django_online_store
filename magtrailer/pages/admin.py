from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'stock', 'available', 'created')  # Общее отображение в админке
    list_filter = ('available', 'category', 'price', 'created', 'updated')  # Фильтровать по этим полям в админке
    list_editable = ('price', 'stock', 'available')  # Изменяемые поля без общего редактирования
    prepopulated_fields = {'slug': ('name', )}  # Одновременное заполнение
    search_fields = ('name', 'category')
    list_display_links = ('name', )


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', )
