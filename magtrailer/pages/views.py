from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import *

menu = [{'title': 'ГОЛОВНА', 'url_name': 'home'},
        {'title': 'ВСІ ПРИЧЕПИ', 'url_name': 'all_categories'},
        {'title': 'ПРО ПІДПРИЄМСТВО', 'url_name': 'about'},
        {'title': 'КОНТАКТИ', 'url_name': 'contacts'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Завод автомобільних причепів MAG Trailer'
    }
    return render(request, 'pages/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'Про підприємство'
    }
    return render(request, 'pages/about.html', context=context)


def categories(request, cat_id=0):
    if cat_id == 0:
        products = Product.objects.filter(available=True)
    else:
        products = Product.objects.filter(category_id=cat_id, available=True)
    context = {
        'menu': menu,
        'products': products,
        'title': 'Наші причепи',
        'cat_selected': cat_id,
    }
    return render(request, 'pages/categories.html', context=context)


def contacts(request):
    return render(request, 'pages/contacts.html', {'menu': menu, 'title': 'Контакти'})


def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    photos = ProductImages.objects.filter(product_id=product_id)
    context = {
        'menu': menu,
        'product': product,
        'photos': photos,
        'title': product.name,
        'cat_selected': product.category_id,
    }
    return render(request, 'pages/product.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена :(</h1>')
