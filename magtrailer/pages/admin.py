from django.contrib import admin
from .models import *


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date', 'is_answer')
    list_filter = ('is_answer',)
    list_editable = ('is_answer',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'available')
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ('available', )
    list_editable = ('available', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'stock', 'available', 'availability')  # Общее отображение в админке
    list_filter = ('available', 'category', 'price', 'created', 'updated', 'availability')  # Фильтровать по этим полям в админке
    list_editable = ('price', 'stock', 'available', 'availability')  # Изменяемые поля без общего редактирования
    prepopulated_fields = {'slug': ('name', )}  # Одновременное заполнение
    search_fields = ('name', 'category')
    list_display_links = ('name', )


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', )
