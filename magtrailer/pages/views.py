from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': 'ГОЛОВНА', 'url_name': 'home'},
        {'title': 'ВСІ ПРИЧЕПИ', 'url_name': 'all_categories'},
        {'title': 'ПРО ПІДПРИЄМСТВО', 'url_name': 'about'},
        {'title': 'КОНТАКТИ', 'url_name': 'contacts'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Main page'
    }
    return render(request, 'pages/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About'
    }
    return render(request, 'pages/about.html', context=context)


def categories(request):
    products = Product.objects.all()
    cat = ['Одноосні', 'Двохосні', 'Спеціалізовані']
    context = {
        'cat': cat,
        'menu': menu,
        'products': products,
        'title': 'Категорії'
    }
    return render(request, 'pages/categories.html', context=context)


def contacts(request):
    return render(request, 'pages/contacts.html', {'menu': menu, 'title': 'Contacts'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена :(</h1>')
