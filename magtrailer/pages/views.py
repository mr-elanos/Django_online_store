from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import *

menu = [{'title': 'ГОЛОВНА', 'url_name': 'home'},
        {'title': 'НАШІ ПРИЧЕПИ', 'url_name': 'all_categories'},
        {'title': 'ПРО НАС', 'url_name': 'about'},
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


def categories(request, cat_slug=None):
    if not cat_slug:
        products = Product.objects.filter(available=True)
    else:
        products = Product.objects.filter(category__slug=cat_slug, available=True)
    context = {
        'menu': menu,
        'products': products,
        'title': 'Наші причепи',
        'cat_selected': cat_slug,
    }
    return render(request, 'pages/categories.html', context=context)


def contacts(request):
    return render(request, 'pages/contacts.html', {'menu': menu, 'title': 'Контакти'})


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    photos = ProductImages.objects.filter(product_id=product.id)
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
